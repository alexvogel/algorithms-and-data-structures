#Uses python3

import sys
#import queue
#import pydot
import os

class Digraph(object):

    '''
        Returns a Graph-object
    '''

    # graph in format 'adjacency list'
    adjacencyList = None

    # graph in format 'edge list'
    edgeList = None

    # amount of vertices
    count_vertices = 0

    # weight
    cost = None

    # holds the distance from startVertex for all vertices
    dist = None

    # holds the information of previous vertex for all vertices
    prev = None

    '''
        constructor
        create a graph object in adjacency list representation
    '''
    def __init__(self, edgeListWithCost, count_vertices):

        # calc adjacency list
        self.adjacencyList = [[] for _ in range(count_vertices)]
        self.edgeList = [[] for _ in range(count_vertices)]
        self.cost = [[] for _ in range(count_vertices)]

        for ((a, b), w) in edgeListWithCost:
            self.adjacencyList[a - 1].append(b - 1)
            self.cost[a - 1].append(w)
            self.edgeList.append([a-1, b-1])

        self.count_vertices = count_vertices

    '''
        bellman-ford algorithm allows to determine shortest paths from startVertex to every other vertex
        it run slowlier than the bfs_dijkstra algorithm, graphs with negative edge weights are possible

        startVertex: vertex id to start the traverse
        returns: -
    '''
    def bfs_bellman_ford(self, startVertex):

        # set dist of all vertices to 'infinity'
        self.dist = [float('inf')] * self.count_vertices

        # set prev for all vertices to none
        self.prev = [None] * self.count_vertices

        # set dist of startVertex to 0
        self.dist[startVertex] = 0

        # repeat for count_vertices - 1 times
        for i in range(0, self.count_vertices - 1):

            # relax every edge
            for current_vertex in range(0, self.count_vertices):

                # go through all edges that leads away from the current vertex
                for i in range(0, len(self.adjacencyList[current_vertex])):

                    # for readability: set the neighbor vertex id
                    pointing_vertex = self.adjacencyList[current_vertex][i]

                    # for readability: set the cost to travel from current to pointing vertex
                    cost_from_current_to_pointing_vertex = self.cost[current_vertex][i]

                    # if a shorter path (current -> pointing vertex) is found, than has been determined to date... 
                    if self.dist[pointing_vertex] > self.dist[current_vertex] + cost_from_current_to_pointing_vertex:

                        # ... store it in the dist list
                        self.dist[pointing_vertex] = self.dist[current_vertex] + cost_from_current_to_pointing_vertex

                        # store the current vertex that has led to the pointing vertex
                        self.prev[pointing_vertex] = current_vertex

    '''
        dijkstra algorithm for determining shortest paths from startVertex to every other vertex
        it runs faster than the bellman-ford algorithm, but it cannot handle negative edge weights (cost)

        startVertex: vertex id to start the traverse
        returns: -
    '''
    def bfs_dijkstra(self, startVertex):

        # set dist of all vertices to 'infinity'
        self.dist = [float('inf')] * self.count_vertices

        # set prev for all vertices to none
        self.prev = [None] * self.count_vertices

        # set dist of startVertex to 0
        self.dist[startVertex] = 0

        # create a datastructure for storing dist values
        # it works as some kind of queue which makes it easy to retrieve the vertex with the smallest dist value
        H = self.dist.copy()
#        H.append(None)

        # initialize infinity to avoid permanent initialization in the while condition
        infinity = float('inf')

        # while there are still vertices in the queue with a distance != infinity
        # in the queue H 'infinity' is the marker that the optimal distance for the corresponding vertex has already been found)
        # unlike in self.dist. there infitity means the vertex is unreachable from startVertex
        while( len([x for x in H if x < infinity]) > 0 ):

            # extract the vertex with the minimum distance as current vertex
            current_vertex = min(range(len(H)), key=H.__getitem__)

            # and set the entry to 'infinity' to mark that the real minimum distance of this vertex has been found
            H[current_vertex] = float('inf')
            
            # go through all edges that leads away from the current vertex
            for i in range(0, len(self.adjacencyList[current_vertex])):

                # for readability: set the neighbor vertex id
                pointing_vertex = self.adjacencyList[current_vertex][i]

                # for readability: set the cost to travel from current to pointing vertex
                cost_from_current_to_pointing_vertex = self.cost[current_vertex][i]

                # if a shorter path (current -> pointing vertex) is found, than has been determined to date... 
                if self.dist[pointing_vertex] > self.dist[current_vertex] + cost_from_current_to_pointing_vertex:

                    # ... store it in the dist list
                    self.dist[pointing_vertex] = self.dist[current_vertex] + cost_from_current_to_pointing_vertex

                    # store the current vertex that has led to the pointing vertex
                    self.prev[pointing_vertex] = current_vertex

                    # update the dist value in the queue.
                    H[pointing_vertex] = self.dist[pointing_vertex]

    '''
        determine if the graph is 'bipartite'
        return: 0 if not, 1 if it is bipartite
    '''
    def minDistance(self, startVertex, targetVertex):
        
        # perform the dijkstra algorithm (a modification of Breadth-First-Search)
        self.bfs_dijkstra(startVertex)

        # after the dijkstra all dist values in self.dist are the optimal real distances from startVertex
        if (self.dist[targetVertex] == float('inf')):
            return -1
        else:
            return self.dist[targetVertex]



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
    edges_with_cost = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))

    digraph = Digraph(edges_with_cost, n)

    data = data[3 * m:]
    startVertex, targetVertext = data[0] - 1, data[1] - 1
    
    print(digraph.minDistance(startVertex, targetVertext))
