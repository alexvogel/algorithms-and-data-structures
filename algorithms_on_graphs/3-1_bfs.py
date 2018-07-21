#Uses python3

import sys
import queue
#import pydot
import os

class Graph(object):

    '''
        Returns a Graph-object
    '''

    # graph in format 'adjacency list'
    adjacencyList = []

    # graph in format 'edge list'
    edgeList = None

    # amount of vertices
    count_vertices = 0

    # distance of vertices from a certain vertex
    dist = None

    '''
        constructor
        create a graph object in adjacency list representation
    '''
    def __init__(self, edgeList, count_vertices):

        # store edge list
        self.edgeList = edgeList

        # calc adjacency list
        self.adjacencyList = [[] for _ in range(count_vertices)]

        for (a, b) in edgeList:
            self.adjacencyList[a - 1].append(b - 1)
            self.adjacencyList[b - 1].append(a - 1)


        self.count_vertices = count_vertices

    '''
        perform a breadth first search
    '''
    def bfs(self, startVertex):

        # set distance of all vertices to infinity
        self.dist = [-1] * self.count_vertices

        # set distance of startVertex to 0
        self.dist[startVertex] = 0

        # create a queue
        q = queue.Queue()

        # put the starting vertex into the queue
        q.put(startVertex)

        while(not q.empty()):

            # retrieve queued vertex as current vertex
            current_vertex = q.get()

            # go through all edges that leads away from the current vertex
            for pointing_vertex in self.adjacencyList[current_vertex]:

                # if distance of pointing vertex is infinity...
                if self.dist[pointing_vertex] == -1:

                    # ... put it in the queue for later processing
                    q.put(pointing_vertex)

                    # and set it's distance accordingly
                    self.dist[pointing_vertex] = self.dist[current_vertex] + 1


    '''
        determine the shortest distance between startVertex and endVertex
        return: distance as integer
    '''
    def distance(self, startVertex, endVertex):
        
        # perform a Breadth-First-Search to determine the distance layer of every vertex relative to startVertex
        self.bfs(startVertex)

        # return the distance of desired vertex (endVertex)
        return self.dist[endVertex]


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
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    graph = Graph(edges, n)

    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    print(graph.distance(s, t))
