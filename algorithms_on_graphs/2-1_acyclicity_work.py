#Uses python3

import sys
import pydot
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
    cycle = 0

    '''
        constructor
        create a graph object in adjacency list representation
    '''
    def __init__(self, edgeList, count_vertices):

        self.edgeList = edgeList

        self.adjacencyList = [[] for _ in range(count_vertices)]
        for (a, b) in self.edgeList:
            self.adjacencyList[a - 1].append(b - 1)

        self.visited = [False] * len(self.adjacencyList)

        self.component_count = [None] * len(self.adjacencyList)

        self.count_vertices = count_vertices

        self.post_order = [None] * len(self.adjacencyList)

        # mark vertices that are sources (no paths leading to it)
        self.sources = [True] * len(self.adjacencyList)

        for targetVertices in self.adjacencyList:
            for vertexIndex in targetVertices:
                self.sources[vertexIndex] = False
        
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
    def dfs(self, x):

        self.visited[x] = True

        self.component_count[x] = self.cc_counter
        print('standing on vertex', x+1, 'connections are', [entry+1 for entry in self.adjacencyList[x]])

        for vertexIndex in self.adjacencyList[x]:

        # if vertex is on stack, then there is a cycle
        

        # if vertex has already been visited, then there must be a cycle
            if self.visited[vertexIndex]:
                print('vertex', vertexIndex, 'already visited')
                self.cycle = 1
            else:
                if self.dfs(vertexIndex) == 1:
                    return 1

        #print('reached a dead end at vertex', x+1)
        self.po_counter += 1
        self.post_order[x] = self.po_counter
        return 0


    '''
        linearize directed graph

        returns: list of vertices
    '''
    def topologicalSortSTUB(self):
        #DFS(G)
        #sort vertices by reverse post-order

        # fully explore graph
        self.dfs(0)

        # create vertices list in post-order
        vertices_post_order = [None] * self.count_vertices
        for i in range(0, self.count_vertices):
            #print('>>', self.post_order[i], ':', 'vertex', i+1)
            vertices_post_order[self.post_order[i]-1] = i

        #print(vertices_post_order)


    '''
        get the indices of all unvisited vertices that have no path leading to them (sources)
        return: list of indices
    '''
    def getSourcesIndicesUnvisited(self):

        # determine all vertices
        result = []

        for i in range(0, self.count_vertices):
            if (self.visited[i] is False) and (self.sources[i] is True):
                result.append(i)

        return result

    '''
        check whether graph contains a cycle
        return: 0 if graph is cyclic, 1 if graph is not cyclic
    '''
    def isCyclic(self):
        
        # fully explore graph
        while(len(self.getSourcesIndicesUnvisited()) > 0):

            self.dfs(self.getSourcesIndicesUnvisited()[0])

        # if there are still unvisited vertices (without any source vertices), there must be cycles
        #print('visited', self.visited)
        print('iscyclic before check visited', self.cycle)
        for isVisited in self.visited:
            if isVisited is False:
                self.cycle = 1

        return self.cycle


    # def connectedComponents(self):
    #     self.cc_counter = 1

    #     self.visited = [False] * len(self.adjacencyList)

    #     for i in range(0, self.count_vertices):
    #         if not self.visited[i]:
    #             self.reach(i)
    #             self.cc_counter = self.cc_counter + 1

    #     return self.cc_counter-1

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
    digraph.plot('graph.png')

    print(digraph.isCyclic())
