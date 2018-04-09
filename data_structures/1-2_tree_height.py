# Uses python3
import argparse
import datetime

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

levels = {}

class Node:

    # constructor
    def __init__(self):
        self.parent = None
        self.root = False
        self.level = None

    def setParent(self, parentnode):
        self.parent = parentnode

    def setRoot(self):
        self.root = True

    def getLevel(self):

        if self.level != None:
            return self.level

        if self.root:
            self.level = 1
        else:
            self.level = self.parent.getLevel() + 1
        
        return self.level

class TreeHeight:

    def __init__(self):

        self.n = None
        self.parent = None

        self.nodes = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

        # create all existent nodes
        self.nodes = [None] * len(self.parent)

        # for every node
        for i in range(0, len(self.parent)):
            
            # create node if not already exists
            if self.nodes[i] == None:
                self.nodes[i] = Node()

            # if root, then set root
            if self.parent[i] == -1:
                self.nodes[i].setRoot()

            # set the parent of current node
            else:
                # create it if necessary
                if self.nodes[self.parent[i]] == None:
                    self.nodes[self.parent[i]] = Node()

                self.nodes[i].setParent(self.nodes[self.parent[i]])

#
    def compute_height_naive(self):
            # Replace this code with a faster implementation
            maxHeight = 0
            for vertex in range(self.n):
                    height = 0
                    i = vertex
                    while i != -1:
                            height += 1
                            i = self.parent[i]
                    maxHeight = max(maxHeight, height);
            return maxHeight;

    def compute_height_fast(self):

            maxHeight = 0

            for i in range(0, len(self.nodes)):
                level = self.nodes[i].getLevel()
                if level > maxHeight:
                    maxHeight = level
                
                #print('level of node ' + str(i) + ' is ' + str(level))

            return maxHeight


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height_fast())


if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-09'

    parser = argparse.ArgumentParser(description='tree height',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)

    args = parser.parse_args()
   
    # this is called when no arguments are used
    threading.Thread(target=main).start()
