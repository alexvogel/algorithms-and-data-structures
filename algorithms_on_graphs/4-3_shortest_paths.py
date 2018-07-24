#Uses python3

import sys
import queue
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

    # marker for being part of a negative cycle True/False
    negativeCycleVertices = None

    # marker for being reachable from a negative cycle True/False
    verticesReachableFromNegativeCycleVertices = None
    

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
        determine the shortest paths from startVertex to every vertex in graph
        bellman-ford algorithm allows to determine shortest paths from startVertex to every other vertex
        it run slowlier than the bfs_dijkstra algorithm, graphs with negative edge weights are possible
        negative cycles

        startVertex: vertex id to start the traverse
        returns: True if a negative cycle exists | False if no negative cycle exists
    '''
    def bfs_bellman_ford_nc_paths(self, startVertex):

        # in case a negative cycle exists in the graph, the vertices will be marked with True
        self.negativeCycleVertices = [False] * self.count_vertices

        # in case a negative cycle exists in the graph, the vertices that are reachable from the negative cycle will be marked with True
        self.verticesReachableFromNegativeCycleVertices = [False] * self.count_vertices

        # set dist of all vertices to 'infinity'
        self.dist = [10**19] * self.count_vertices
        #self.dist = [float('inf')] * self.count_vertices

        # set prev for all vertices to none
        self.prev = [None] * self.count_vertices

        # set dist of startVertex to 0
        self.dist[startVertex] = 0

        # list of vertex ids that are part of a negative cycle
        negative_cycle_vertex_ids = []

        # the shortests paths are found in at most (count_vertices - 1) iterations
        # if there is a relaxation on the (count_vertices)th iteration, there must be a negative cycle
        # to capture the vertices of the negative cycle, the next count_vertices times are to mark the vertices of the negative cycle
        first_iteration_for_search_of_negative_cycle = False
        for i in range(0, self.count_vertices + 1):

            if i == self.count_vertices - 1:
                first_iteration_for_search_of_negative_cycle = True

            # relax every edge
            for current_vertex in range(0, self.count_vertices):

                # go through all edges that leads away from the current vertex
                for j in range(0, len(self.adjacencyList[current_vertex])):

                    # for readability: set the neighbor vertex id
                    pointing_vertex = self.adjacencyList[current_vertex][j]

                    # for readability: set the cost to travel from current to pointing vertex
                    cost_from_current_to_pointing_vertex = self.cost[current_vertex][j]

                    # if a shorter path (current -> pointing vertex) is found, than has been determined to date... 
                    # perform relaxation if ...
                    if self.dist[current_vertex] == 10**19:
                        next

                    elif self.dist[pointing_vertex] > self.dist[current_vertex] + cost_from_current_to_pointing_vertex:

                        # if it is the first iteration in the search of a negative cycle, a negative cycle is present
                        # and the vertices that make it are being marked
                        if first_iteration_for_search_of_negative_cycle:

                            # if a vertex is already marked as part of a negative cycle, the search can end
                            if self.negativeCycleVertices[pointing_vertex]:
                                break

                            # else: mark the pointing_vertex as part of a negative cycle
                            else:
                                self.negativeCycleVertices[pointing_vertex] = True
                                negative_cycle_vertex_ids.append(pointing_vertex)

                        # ... store it in the dist list
                        self.dist[pointing_vertex] = self.dist[current_vertex] + cost_from_current_to_pointing_vertex

                        # store the current vertex that has led to the pointing vertex
                        self.prev[pointing_vertex] = current_vertex

        # for all vertices that are part of the negative cycle
        # a Breadth-First-Search is performed to determine all vertices
        # that are reachable from any vertex of the negative cycle
        vertices_reachable_from_negative_cycle = self.bfs_reachable(negative_cycle_vertex_ids)

        # mark them as true
        for vertex in vertices_reachable_from_negative_cycle:
            self.verticesReachableFromNegativeCycleVertices[vertex] = True

        #print(self.verticesReachableFromNegativeCycleVertices)

    '''
        perform a breadth first search
        startVertices: list of vertex ids from where the breadth first search should start
        returns: vertices, that are reachable from startVertices
    '''

    def bfs_reachable(self, startVertices):

        # the result list with all vertices that are reachable from startVertices
        vertices_reachable = []

        # create a queue
        q = queue.Queue()

        # add startVertices to queue
        for currentVertex in startVertices:
            # put the starting vertices into the queue
            q.put(currentVertex)

        while(not q.empty()):

            # retrieve queued vertex as current vertex
            current_vertex = q.get()

            #print('current vertex', current_vertex)

            vertices_reachable.append(current_vertex)

            # go through all edges that leads away from the current vertex
            for pointing_vertex in self.adjacencyList[current_vertex]:

                    # ... put it in the queue for later processing if it is not already in the list of vertices reachable
                    if pointing_vertex not in vertices_reachable:
                        q.put(pointing_vertex)

        # return the list of all reachable vertices from startVertices
        return vertices_reachable


    '''
        determine if a negative cycle in graph exists
        bellman-ford algorithm allows to determine shortest paths from startVertex to every other vertex
        it run slowlier than the bfs_dijkstra algorithm, graphs with negative edge weights are possible

        startVertex: vertex id to start the traverse
        returns: True if a negative cycle exists, False if no negative cycle exists
    '''
    def bfs_bellman_ford_negative_cycle(self, startVertex):

        # set dist of all vertices to 'infinity'
        #self.dist = [float('inf')] * self.count_vertices
        # in some case float(inf) does not work to detect negative cycles
        self.dist = [10**19] * self.count_vertices

        # set prev for all vertices to none
        self.prev = [None] * self.count_vertices

        # set dist of startVertex to 0
        self.dist[startVertex] = 0

        # the shortests paths are found in at most (count_vertices - 1) iterations
        # if there is a relaxation on the (count_vertices)th iteration, there must be a negative cycle
        last_iteration = False
        for i in range(0, self.count_vertices):

            if i == self.count_vertices - 1:
                last_iteration = True

            # relax every edge
            for current_vertex in range(0, self.count_vertices):

                # go through all edges that leads away from the current vertex
                for j in range(0, len(self.adjacencyList[current_vertex])):

                    # for readability: set the neighbor vertex id
                    pointing_vertex = self.adjacencyList[current_vertex][j]

                    # for readability: set the cost to travel from current to pointing vertex
                    cost_from_current_to_pointing_vertex = self.cost[current_vertex][j]

                    # if a shorter path (current -> pointing vertex) is found, than has been determined to date... 
                    # perform relaxation if ...
                    if self.dist[pointing_vertex] > self.dist[current_vertex] + cost_from_current_to_pointing_vertex:

                        # if there is a relaxation on the last iteration, then there must exist a negative cycle
                        if last_iteration is True:
                            return True

                        # ... store it in the dist list
                        self.dist[pointing_vertex] = self.dist[current_vertex] + cost_from_current_to_pointing_vertex

                        # store the current vertex that has led to the pointing vertex
                        self.prev[pointing_vertex] = current_vertex

        # if bellman-ford runs through all relaxations in count_vertices-1 times, there is no negative cycle in the graph
        return False

    '''
        bellman-ford algorithm allows to determine shortest paths from startVertex to every other vertex
        it run slowlier than the bfs_dijkstra algorithm, graphs with negative edge weights are possible
        no negative cycles are allowed

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
                for j in range(0, len(self.adjacencyList[current_vertex])):

                    # for readability: set the neighbor vertex id
                    pointing_vertex = self.adjacencyList[current_vertex][j]

                    # for readability: set the cost to travel from current to pointing vertex
                    cost_from_current_to_pointing_vertex = self.cost[current_vertex][j]

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
        determine the shortest path from startVertex to targetVertex
        return: pathlength as integer, -1 if targetVertex is not reachable
    '''
    def minDistance(self, startVertex, targetVertex):
        
        # perform the dijkstra algorithm (a modification of Breadth-First-Search) to determine the shortest paths from startVertex to every vertex in the graph
        self.bfs_dijkstra(startVertex)

        # after the dijkstra all dist values in self.dist are the optimal real distances from startVertex
        if (self.dist[targetVertex] == float('inf')):
            return -1
        else:
            return self.dist[targetVertex]

    '''
        determine whether graph has a negative cycle or not by using a modified Bellman-Ford Algorithm
        return: 0 if no negative cycle, 1 if a negative cycle is detected
    '''
    def hasNegativeCycle(self):

        if self.bfs_bellman_ford_negative_cycle(0):
            return 1
        else:
            return 0

    '''
        determine the shortest paths from startVertex to every other vertex
        negative weights and negative cycles are allowed
        prints the distances from startVertex to all other vertices
        '-' means '-infinity'
        '*' means vertex is not reachable from startVertex (=infinity)

        returns: -
    '''
    def printShortestPaths(self, startVertex):

        # perform
        self.bfs_bellman_ford_nc_paths(startVertex)

        for vertex in range(0, self.count_vertices):

            #print(vertex+1, ':', end='')

            # distances are -infinity
            if self.verticesReachableFromNegativeCycleVertices[vertex]:
                print('-')

            # vertices are not reachable (=infinity marked as 10**19)
            elif self.dist[vertex] == float('inf') or self.dist[vertex] == 10**19:
                print('*')

            # vertices are reachable and not part of the negative cycle
            else:
                print(self.dist[vertex])



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

    '''
    input format is
    line 1: number_of_vertices number_of_edges
    line 2->x: from_vertex to_vertex edge_weight
    line x+1: startVertex
    '''

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))

    digraph = Digraph(edges, n)

    #digraph.plot('digraph.png')
#    data = data[3 * m:]

    startVertex = data[-1]
    startVertex -= 1

    digraph.printShortestPaths(startVertex)
