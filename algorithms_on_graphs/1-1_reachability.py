#Uses python3

import sys

#import pydot
import os

class Graph(object):

    '''
        Returns a Graph-object
    '''

    # fields of object
    adjacencyList = []
    edgeList = None
    visited = None
    count_vertices = 0
    cc = []

    cc_counter = 0

    '''
        constructor
        create a graph object in adjacency list representation
    '''
    def __init__(self, edgeList, count_vertices):

        self.edgeList = edgeList


        self.adjacencyList = [[] for _ in range(count_vertices)]

        for (a, b) in edgeList:
            self.adjacencyList[a - 1].append(b - 1)
            self.adjacencyList[b - 1].append(a - 1)


        self.visited = [False] * len(self.adjacencyList)

        self.cc = [None] * len(self.adjacencyList)

        self.count_vertices = count_vertices

    '''
        check whether there is a path from one vertex to another
        if there is a path return 1
        if there is NO path return 0
        x: starting vertex
        y: ending vertex
    '''
    def reach(self, x, y=None):

        self.visited[x] = True
        self.cc[x] = self.cc_counter
#        print('standing on vertex', x+1, 'looking for vertex', y+1, 'connections are', [entry+1 for entry in self.adjacencyList[x]])

        if y is not None and y in self.adjacencyList[x]:
#            print('SUCCESS: found verex', y+1, '- coming from vertex', x+1)
            return 1

        for vertexIndex in self.adjacencyList[x]:
            if not self.visited[vertexIndex]:
                if self.reach(vertexIndex, y) == 1:
                    return 1

#        print('reached a dead end at vertex', x+1)
        return 0


    def connectedComponents(self):
        self.cc_counter = 1

        self.visited = [False] * len(self.adjacencyList)

        for i in range(0, self.count_vertices):
            if not self.visited[i]:
                self.reach(i)
                self.cc_counter = self.cc_counter + 1

        return self.cc_counter-1

    def plot(self, pngfile):

        # create a pydot graph
        pydot_graph = pydot.Dot(graph_type="graph")

        # add all vertices
        for i in range(0, self.count_vertices):
            pydot_graph.add_node(pydot.Node(i+1, label=i+1))

        for edge in self.edgeList:

            pydot_edge = pydot.Edge(edge[0], edge[1])
            pydot_graph.add_edge(pydot_edge)

        pydot_graph.write_png(pngfile)


if __name__ == '__main__':

    # the graph is read from stdin in edge list format
    # first the edge list is converted into an adjacency list representation of the graph
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    
    x, y = x - 1, y - 1

    # create graph object
    graph = Graph(edges, n)

    # plot graph to debug
#    graph.plot('graph.png')

    print(graph.reach(x, y))

