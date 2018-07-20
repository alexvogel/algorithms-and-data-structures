#Uses python3

import sys
#import pydot
import os


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

    # component count. each vertex is part of a component. components are unconnected zones in a graph
    component_count = []

    # running counter when traversing through the graph
    cc_counter = 0

    # post-order vertices
    post_order = []

    # post-order vertices
    po_counter = 0

    # marker for graph being a cyclic
    cycle_marker = 0

    # vertices on a cycle, if a cycle exists
    cycle = []

    # vertices on function-call stack
    onStack = []

    edgeTo = []

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

        self.visited = [False] * self.count_vertices

        self.component_count = [None] * self.count_vertices

        self.post_order = [None] * self.count_vertices

        # mark vertices that are sources (no paths leading to it)
        self.sources = [True] * self.count_vertices

        for targetVertices in self.adjacencyList:
            for vertexIndex in targetVertices:
                self.sources[vertexIndex] = False
        
        # set all vertices to False
        self.onStack = [False] * self.count_vertices

        self.edgeTo = [None] * self.count_vertices


        # debug
        #print('adjacencyList', self.adjacencyList)
        #print('sources', self.sources)

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

        #print('standing on vertex', v+1, 'connections are', [entry+1 for entry in self.adjacencyList[v]])

        # for all vertices that are reachable from v
        for w in self.adjacencyList[v]:
            #print('length of self.cycle', len(self.cycle))
            if len(self.cycle) > 0:
                return
            elif not self.visited[w]:
                self.edgeTo[w] = v
                self.dfs(w)
            elif self.onStack[w]:
                self.cycle = []

                x = v
                while(x != w):
                    self.cycle.insert(0, x)
                    x = self.edgeTo[x]

                self.cycle.insert(0, w)
                self.cycle.insert(0, v)

        #print('cycle', self.cycle)

        # set cyclic marker if cycle detected
        if len(self.cycle) > 0:
            self.cycle_marker = 1
        self.onStack[v] = False

        # # increase post order counter
        # po_counter += 1

        # # and set po counter to vertix 
        # self.post_order[v] = po_counter


    '''
        linearize directed graph

        returns: list of vertices
    '''
    # def topologicalSortSTUB(self):
    #     #DFS(G)
    #     #sort vertices by reverse post-order

    #     # fully explore graph
    #     self.dfs(0)

    #     # create vertices list in post-order
    #     vertices_post_order = [None] * self.count_vertices
    #     for i in range(0, self.count_vertices):
    #         #print('>>', self.post_order[i], ':', 'vertex', i+1)
    #         vertices_post_order[self.post_order[i]-1] = i

    #     #print(vertices_post_order)


    '''
        check whether graph contains a cycle
        return: 0 if graph is cyclic, 1 if graph is not cyclic
    '''
    def isCyclic(self):
        
        for v in range(0, self.count_vertices):
            if not self.visited[v]:
                self.dfs(v)

        return self.cycle_marker


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



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    digraph = Digraph(edges, n)
    #digraph.plot('graph.png')

    print(digraph.isCyclic())
