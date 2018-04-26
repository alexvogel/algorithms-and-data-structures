# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.parent = [-1 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

      # set parents
      if b != -1:
        self.parent[b] = i
      if c != -1:
        self.parent[c] = i

  # this traverses the tree recursivly in this order:
  # 1) left child
  # 2) the node itself
  # 3) right child
  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that

    # start with root
    self.inOrderTraversal(0)

    return self.result

  # this traverses the tree recursivly in this order:
  # 1) the node itself
  # 2) left child
  # 3) right child
  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that

    # start with root
    self.preOrderTraversal(0)

    return self.result

  # this traverses the tree recursivly in this order:
  # 1) left child
  # 2) right child
  # 3) the node itself
  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
                
    # start with root
    self.postOrderTraversal(0)

    return self.result

  def inOrderTraversal(self, i):

    if self.left[i] != -1:
      self.inOrderTraversal(self.left[i])

    self.result.append(self.key[i])

    if self.right[i] != -1:
      self.inOrderTraversal(self.right[i])


  # get the nodes of tree i in pre order
  def preOrderTraversal(self, i):

    self.result.append(self.key[i])

    if self.left[i] != -1:
      self.preOrderTraversal(self.left[i])
    if self.right[i] != -1:
      self.preOrderTraversal(self.right[i])

  # get the nodes of tree i in post order
  def postOrderTraversal(self, i):

    if self.left[i] != -1:
      self.postOrderTraversal(self.left[i])
    if self.right[i] != -1:
      self.postOrderTraversal(self.right[i])

    self.result.append(self.key[i])


  # get Node with next higher key
  def nextNode(self, i):

    if self.right[i] != -1:
      return self.leftDescendant(self.right[i])
    else:
      return self.rightAncestor(i)


  # get the most deepest left node of tree i
  def leftDescendant(self, i):
    if self.left[i] == -1:
      return i
    else:
      return self.leftDescendant(self.left[i])

  # get the parent node, if i is the left child
  # get the parent node of the parent, if i is the right child
  def rightAncestor(self, i):

    if i == -1:
      return -1

    if self.key[i] < self.key[self.parent[i]]:
      return self.parent[i]
    else:
      return self.rightAncestor(self.parent[i])

  # find the node with key=searchKey
  def findNode(self, searchKey, i):
    if self.key[i] == searchKey:
      return i
    elif self.key[i] > searchKey:
      if self.left[i] != -1:
        return self.findNode(searchKey, self.left[i])
    elif self.key[i] < searchKey:
      return self.findNode(searchKey, self.right[i])

  # find the node with the smallest key of tree i
  def findNodeMinKey(self, i):
    if self.left[i] != -1:
      self.findNodeMinKey(self.left[i])
    else:
      return i



def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()


'''
### 6.1 Binary tree traversals

#### Problem Introduction
In this problem you will implement in-order, pre-order and post-order traversals of a binary tree. These traversals were defined in the week 1 lecture on tree traversals, but it is very useful to practice implementing them to understand binary search trees better.

#### Problem Description
**Task:** You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.    
**Input Format:** The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n − 1. Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n − 1 in order. Each of these lines contains three integers key i , lef t i and right i — key i is the key of the i-th vertex, lef t i is the index of the left child of the i-th vertex, and right i is the index of the right child of the i-th vertex. If i doesn’t have left or right child (or both), the corresponding lef t i or right i (or both) will be equal to −1.  
**Constraints:** 1 ≤ n ≤ 10^5 ; 0 ≤ key i ≤ 10^9 ; −1 ≤ left_i , right_i ≤ n − 1. It is guaranteed that the input represents a valid binary tree. In particular, if lef t i ̸ = −1 and right i ̸ = −1, then lef t i ̸ = right i . Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex.  
**Output Format:** Print three lines. The first line should contain the keys of the vertices in the in-order traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.  
**Time Limits:** language C C++ Java Python C# Haskell JavaScript Ruby Scala time (sec) 1 1 12 6 1.5 2 6 6 12  
**Memory Limit:** 512MB.  

#### Sample 1

*Input:*  
5  
4 1 2  
2 3 4  
5 -1 -1  
1 -1 -1  
3 -1 -1  

*Output:*  
1 2 3 4 5  
4 2 1 3 5  
1 3 2 5 4  

**Explanation:**  
         4
        / \
       2   5
      / \
     1   3

#### Sample 2

*Input:*  
10  
0 7 2  
10 -1 -1  
20 -1 6  
30 8 9  
40 3 -1  
50 -1 -1  
60 1 -1  
70 5 4  
80 -1 -1  
90 -1 -1  

*Output:*  
50 70 80 30 90 40 0 20 10 60  
0 70 50 40 30 80 90 20 60 10  
50 80 90 30 40 70 10 60 20 0  

**Explanation:**
          0
         / \
        70  20
       /  \   \
      50   40  60
           /   /
         30   10
         / \
        80  90

#### What to Do
Implement the traversal algorithms from the lectures. Note that the tree can be very deep in this problem, so you should be careful to avoid stack overflow problems if you’re using recursion, and definitely test your solution on a tree with the maximum possible height.

#### Implementation in Python

[6-1_tree_orders.py](6-1_tree_orders.py)

'''