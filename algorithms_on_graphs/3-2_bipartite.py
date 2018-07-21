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
    side = None

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
    def bfs_bipartite(self, startVertex):

        # set side of all vertices to None
        self.side = [None] * self.count_vertices

        # set side of startVertex to 1 (left)
        self.side[startVertex] = 1

        # create a queue
        q = queue.Queue()

        # put the starting vertex into the queue
        q.put(startVertex)

        while(not q.empty()):

            # retrieve queued vertex as current vertex
            current_vertex = q.get()

            # go through all edges that leads away from the current vertex
            for pointing_vertex in self.adjacencyList[current_vertex]:

                # if side of pointing vertex is None...
                if self.side[pointing_vertex] == None:

                    # set it to the opposite side of current vertex (* -1)
                    self.side[pointing_vertex] = -1 * self.side[current_vertex]

                    # ... and add it to the queue for later processing
                    q.put(pointing_vertex)

                # if side of pointing vertex is already known and the same as of the current vertex, the graph is NOT biparte
                elif self.side[pointing_vertex] == self.side[current_vertex]:
                    return False

        return True

    '''
        determine if the graph is 'bipartite'
        return: 0 if not, 1 if it is bipartite
    '''
    def isBipartite(self):
        
        # perform a Breadth-First-Search to explore the graph starting at vertex 0
        if self.bfs_bipartite(0):
            return 1
        else:
            return 0


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

    print(graph.isBipartite())
