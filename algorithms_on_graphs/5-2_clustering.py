#Uses python3
import sys
import math
#import pydot

'''
    datastructure for disjoint sets

'''


class DisjointSets(object):

    # a list of sets
    sets = []

    # register item->set
    item_set = {}

    # marked sets
    markedSets = None

    '''
        constructor
    '''
    def __init__(self, listItems):

        # create a set for every item and add it to the list of sets
        for item in listItems:
            mySet = {item}
            self.sets.append(mySet)

            # register the item
            self.item_set[item] = len(self.sets) - 1

    '''
        are items in same set
        if they are in different sets, mark these 2 sets for later use
        return True if items are in same set. False if items are not in same set
    '''
    def sameSet(self, item_a, item_b):

        if self.item_set[item_a] == self.item_set[item_b]:
            return True
        else:
            return False

    '''
        set_id of an item
        return: set_id
    '''
    def setOfItem(self, item):
        return self.item_set[item]


    '''
        merge content of set_b into set set_a. delete set_b
        return: -
    '''
    def merge(self, set_id_a, set_id_b):

        # add the content of set b to set a
        #print(len(self.sets), 'id set a', set_id_a, 'id_set_b', set_id_b)
        self.sets[set_id_a].update(self.sets[set_id_b])

        # remove set b from list of all sets
        # and change entries in register
        for i in self.sets[set_id_b]:
            self.item_set[i] = set_id_a

        self.sets[set_id_b] = None

    def print(self):

        print('list of all sets')
        for i in range(0, len(self.sets)):

            print(i, ':', self.sets[i])




class Graph(object):

    '''
        Returns a Graph-object
    '''

    # graph in format 'adjacency list'
    adjacencyList = None

    # graph in format 'edge list'
    edges_sorted = None

    # amount of vertices
    count_vertices = 0

    # weight
    costs_sorted = None

    # is the minimum distance between all clusters
    min_dist_cluster = None    

    # edges and costs for use in clustering
    edges_deleted = None
    costs_deleted = None


    '''
        constructor
        create a graph object in adjacency list representation
        x: x coordinates of vertices
        y: y coordinates of vertices
    '''
    def __init__(self, x, y):

        # set amount of vertices
        self.count_vertices = len(x)

        # create edges and costs, both sorted by costs
        self.costs_sorted = []
        self.edges_sorted = []

        edges = []
        costs = []

        # go through all vertices
        # create adjacencyList, edgeList and costs
        for vertex_from_id in range(0, self.count_vertices):

            for vertex_to_id in range( vertex_from_id+1, self.count_vertices):

                w = math.sqrt(math.pow(x[vertex_from_id] - x[vertex_to_id], 2) + math.pow(y[vertex_from_id] - y[vertex_to_id], 2))

                edges.append([vertex_from_id, vertex_to_id])
                costs.append(w)

        # zip weights and edges together
        costs_and_edges = list(zip(costs, edges))

        # sort the combined list
        costs_and_edges.sort()

        # costs sorted
        self.costs_sorted = [costs for costs, edges in costs_and_edges]

        # costs sorted
        self.edges_sorted = [edges for costs, edges in costs_and_edges]

        #print(self.adjacencyList)
        #print(self.cost)
        #print(self.costs_sorted)
        #print(self.edges_sorted)


    '''
        determine the length of the minimum-spanning-tree
    '''
    def msp_length(self):

        # create a graph from self that is a minimum spanning tree
        graph_msp = self.msp_kruskal()

        return graph_msp.length_all_edges()

    '''
        create a Minimum-Spanning-Tree from the 'self'-graph by using the kruskal algorithm
        return: graph of the MSP
    '''
    def msp_kruskal(self):

        # msp_graph
        msp_graph = Graph([], [])

        # create a disjoint set which puts every vertex in its own set
        myDisjointSets = DisjointSets(range(0, self.count_vertices))

        # go through the edges (sorted by costs from lowest to highest)
        for i in range(0, len(self.edges_sorted)):

            # i is currently the shortest edge in the graph

            # if vertices of the shortest edge ly in different sets, then it is a safe move to add this edge and the vertex to msp
            if not myDisjointSets.sameSet(self.edges_sorted[i][0], self.edges_sorted[i][1]):

                # add new edge to graph X that contains the MSP
                msp_graph.add_edge(self.edges_sorted[i], self.costs_sorted[i])

                # merge the two sets
                myDisjointSets.merge(myDisjointSets.setOfItem(self.edges_sorted[i][0]), myDisjointSets.setOfItem(self.edges_sorted[i][1]) )


        #myDisjointSets.print()
        return msp_graph

    '''
        from the given graph (self) create a graph that is devided in k cluster
        return: clustered graph
    '''
    def cluster(self, k):

        # create a minimum spanning tree with Kruskal's Algorithm
        msp_graph = self.msp_kruskal()

        # number of edges to delete
        n_delete = k-1

        # cluster it by deleting the k-1 longest edges
        # the minimum distance between all clusters is the -k_th edge_length (cost/weight/length)
        msp_graph.min_dist_cluster = msp_graph.costs_sorted[-1 * n_delete]

        # delete the k longest edges
        del(msp_graph.edges_sorted[-1 * n_delete:])
        del(msp_graph.costs_sorted[-1 * n_delete:])

        # return the clustered graph to caller
        return msp_graph


    '''
        determines the length of all edges (sum of all costs/length/weights)
    '''
    def length_all_edges(self):

        return sum(self.costs_sorted)

    '''
        add an edge and its cost to the graph
        they are UNSORTED
    '''
    def add_edge(self, edge, cost):
        
        #
        self.edges_sorted.append(edge)
        self.costs_sorted.append(cost)

    def plot(self, pngfile):

        # create a pydot graph
        pydot_graph = pydot.Dot(graph_type="graph")

        # add all vertices
        for i in range(0, self.count_vertices):
            pydot_graph.add_node(pydot.Node(i+1, label=i+1))

        for edge in self.edges_sorted:

            pydot_edge = pydot.Edge(edge[0], edge[1])
            pydot_graph.add_edge(pydot_edge)

        pydot_graph.write_png(pngfile)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]

    undirected_graph = Graph(x, y)

    k = data[-1]

    clustered_graph = undirected_graph.cluster(k)

#    data = data[2 * n:]

    print("{0:.9f}".format(clustered_graph.min_dist_cluster))

