#Uses python3

import sys
#import pydot
import os

sys.setrecursionlimit(200000)


class Digraph(object):

    '''
        Returns a Directed Graph-object
    '''

    # fields of object

    # graph in format adjacency list
    adjacencyList = []

    # graph in format edge list
    edgeList = None

    # # marker if a vertex has been visited
    visited = None

    # total amount of vertices
    count_vertices = 0

    # strongly component count. each vertex is part of a component.
    scc = []

    # running counter for scc
    scc_counter = 0

    # visit counter
    visit_counter = None

    # post-order vertices
    previsit_order = []

    # post-order vertices
    postvisit_order = []

    # marker for graph being a cyclic
    cycle_marker = 0

    # vertices on a cycle, if a cycle exists
    cycle = []

    # vertices on function-call stack
    onStack = []

    edgeTo = []

    # vertices in toposort order
    toposort_order = []

    '''
        constructor
        create a graph object in adjacency list representation
    '''
    def __init__(self, edgeList, count_vertices):

        self.count_vertices = count_vertices

        self.edgeList = edgeList

        self.adjacencyList = [[] for _ in range(count_vertices)]
        for (a, b) in self.edgeList:
            self.adjacencyList[a - 1].append(b - 1)

        # mark vertices that are sources (no paths leading to it)
        self.sources = [True] * self.count_vertices

        for targetVertices in self.adjacencyList:
            for vertexIndex in targetVertices:
                self.sources[vertexIndex] = False
        
        self.resetAllCounters()

        # debug
        #print('adjacencyList', self.adjacencyList)
        #print('sources', self.sources)

    def resetAllCounters(self):


        self.visit_counter = 0
        self.previsit_order = [None] * self.count_vertices

        self.postvisit_order = [None] * self.count_vertices

        self.visited = [None] * self.count_vertices
        # set all vertices to False
        self.onStack = [False] * self.count_vertices

        self.edgeTo = [None] * self.count_vertices

        self.component_count = [None] * self.count_vertices
        self.cc_counter = 0

        self.toposort_order = [None] * self.count_vertices

        self.scc = [None] * self.count_vertices
        self.scc_counter = 0


    '''
        return: edgeList with reversed directions
    '''

    def reverseEdges(self):

        reversedEdgeList = []

        for edge in self.edgeList:
            reversedEdgeList.append([edge[1], edge[0]])

        return reversedEdgeList

    '''
        compute Strongly Connected Components
    '''
    def getSccCount(self):

        # create a reversed graph
        digraphR = Digraph(self.reverseEdges(), self.count_vertices)

        # debug
        #digraphR.plot('graph_reversed.png')

        toposort_graphR = digraphR.getToposort(breakIfCycle=False)

        # print('previsit_order_graphR', digraphR.previsit_order)
        # print('postvisit_order_graphR', digraphR.postvisit_order)
        # print('toposort_graphR', toposort_graphR)

        for v in toposort_graphR:
            if not self.visited[v]:
                # increment the counter of Strongly-Connected-Component
                self.scc_counter += 1
                # dfs through all reachable vertices of the current sink component
                self.dfs(v)

        return self.scc_counter

    '''
        check whether there is a path from one vertex to another
        in Depth-First-Search DFS
        if there is a path return 1
        if there is NO path return 0
        x: vertex to start exploration from
    '''
    def dfs(self, v):

        self.onStack[v] = True
        self.visited[v] = True

        self.visit_counter += 1
        self.previsit_order[v] = self.visit_counter

        #print('exploring', v, 'setting its scc to', self.scc_counter)
        self.scc[v] = self.scc_counter

        #print('standing on vertex', v+1, 'connections are', [entry+1 for entry in self.adjacencyList[v]])

        # for all vertices that are reachable from v
        for w in self.adjacencyList[v]:
            if not self.visited[w]:
                self.dfs(w)

        # marking that vertex is off the stack
        self.onStack[v] = False

        # increase post order counter
        self.visit_counter += 1

        # and set po counter to vertix 
        self.postvisit_order[v] = self.visit_counter
        #print('vertex', v, 'has post order', self.visit_counter)
        #print(self.post_order)



    '''
        check whether graph contains a cycle
        return: 0 if graph is cyclic, 1 if graph is not cyclic
    '''
    def isCyclic(self):
        
        for v in range(0, self.count_vertices):
            if not self.visited[v]:
                self.dfs(v)

        return self.cycle_marker


    '''
        toposort all vertices. linearize directed graph
        return: list with vertex indices in linearized order
    '''
    def getToposort(self, breakIfCycle=True):

        for v in range(0, self.count_vertices):
            if not self.visited[v]:
                self.dfs(v)

        #print('onStack', self.onStack)

        if breakIfCycle and self.cycle_marker:
            print('ERROR: directed graph is cyclic and toposort cannot be performed')
            return None

        #print('previsit order:', self.previsit_order)
        #print('postvisit order:', self.postvisit_order)

        #tmp_postvisit_order = self.postvisit_order.copy()

        # create a dict with postvisit_counter -> vertex_index
        postvisit_counter_vertex_index = {}
        for i in range(0, self.count_vertices):
            postvisit_counter_vertex_index[self.postvisit_order[i]] = i

        #print('postvisit_order', self.postvisit_order)

        # get a reversed sorted list from postvisit counts
        postvisit_counter_reversed_sorted = list(reversed(sorted(self.postvisit_order)))

        # create a list of vertex indices that is toposort
        for i in range(0, self.count_vertices):
            self.toposort_order[i] = postvisit_counter_vertex_index[postvisit_counter_reversed_sorted[i]]


        # for i in range(0, self.count_vertices):

        #     index_of_vertice_with_max_postvisit_counter = max(range(len(tmp_postvisit_order)), key=tmp_postvisit_order.__getitem__)
        #     self.toposort_order.append(index_of_vertice_with_max_postvisit_counter)

        #     tmp_postvisit_order[index_of_vertice_with_max_postvisit_counter] = -1


        #print('toposort order:', self.toposort_order)

#        print('toposort:', list(reversed(self.postvisit_order)))

        return self.toposort_order

    def plot(self, pngfile):

        # create a pydot graph
        pydot_graph = pydot.Dot(graph_type="digraph")

        # add all vertices
        for i in range(0, self.count_vertices):
            pydot_graph.add_node(pydot.Node(i+1, label=i+1))

        for edge in self.edgeList:

            pydot_edge = pydot.Edge(edge[0], edge[1])
            pydot_graph.add_edge(pydot_edge)

        pydot_graph.write_png(pngfile)




def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    digraph = Digraph(edges, n)

    # debug
    #digraph.plot('graph.png')

    print(digraph.getSccCount())
