#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def IsBinarySearchTree(tree, index=0, lowerBound=float("-inf"), upperBound=float("inf")):
  # Implement correct algorithm here

  if len(tree) == 0:
    return True

  # print('---')
  # print('lowerBound=' + str(lowerBound))
  # print('upperBound=' + str(upperBound))
  # print('node=' + str(tree[index]))

  if tree[index][0] <= lowerBound or tree[index][0] >= upperBound:
    return False

  leftIsBinarySearchTree = True
  if tree[index][1] != -1:
    leftIsBinarySearchTree = IsBinarySearchTree(tree, tree[index][1], lowerBound, tree[index][0])
  
  rightIsBinarySearchTree = True
  if tree[index][2] != -1:
    rightIsBinarySearchTree = IsBinarySearchTree(tree, tree[index][2], tree[index][0], upperBound)

  if not leftIsBinarySearchTree or not rightIsBinarySearchTree:
    return False

  return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))

  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()


'''

### 6.2 Is it a binary search tree?

#### Problem Introduction
In this problem you are going to test whether a binary search tree data structure from some programming language library was implemented correctly. There is already a program that plays with this data structure by inserting, removing, searching integers in the data structure and outputs the state of the internal binary tree after each operation. Now you need to test whether the given binary tree is indeed a correct binary search tree. In other words, you want to ensure that you can search for integers in this binary tree using binary search through the tree, and you will always get correct result: if the integer is in the tree, you will find it, otherwise you will not.

#### Problem Description
**Task**. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary search tree. The definition of the binary search tree is the following: for any node of the tree, if its key is x, then for any node in its left subtree its key must be strictly less than x, and for any node in its right subtree its key must be strictly greater than x. In other words, smaller elements are to the left, and bigger elements are to the right. You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a tree, and each node has at most two children.
**Input Format**. The first line contains the number of vertices n. The vertices of the tree are numbered from 0 to n − 1. Vertex 0 is the root. The next n lines contain information about vertices 0, 1, ..., n − 1 in order. Each of these lines contains three integers key i , lef t i and right i — key i is the key of the i-th vertex, lef t i is the index of the left child of the i-th vertex, and right i is the index of the right child of the i-th vertex. If i doesn’t have left or right child (or both), the corresponding lef t i or right i (or both) will be equal to −1.
**Constraints**. 0 ≤ n ≤ 10^5 ; −2^31 < key i < 2^31 − 1; −1 ≤ lef t i , right i ≤ n − 1. It is guaranteed that the input represents a valid binary tree. In particular, if lef t i ̸ = −1 and right i ̸ = −1, then lef t i ̸ = right i . Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex. All keys in the input will be different.
**Output Format**. If the given binary tree is a correct binary search tree (see the definition in the problem description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).

#### Sample 1

*Input:*  
3  
2 1 2  
1 -1 -1  
3 -1 -1  

*Output:*  
CORRECT  

**Explanation:**  
          2  
        /   \  
       1     3  

Left child of the root has key 1, right child of the root has key 3, root has key 2, so everything to the left is smaller, everything to the right is bigger.

#### Sample 2

*Input:*
3  
1 1 2  
2 -1 -1  
3 -1 -1  

*Output:*  
INCORRECT  

**Explanation:**  
        1
       / \
      2   3

The left child of the root must have smaller key than the root.

#### Sample 3

*Input:*  
0  

*Output:*  
CORRECT

**Explanation:**  

Empty tree is considered correct.

#### Sample 4

*Input:*  
5  
1 -1 1  
2 -1 2  
3 -1 3  
4 -1 4  
5 -1 -1  

*Output:*  
CORRECT  

**Explanation:**
        1
         \
          2
           \
            3
             \
              4
               \
                5

The tree doesn’t have to be balanced. We only need to test whether it is a correct binary search tree, which the tree in this example is.

#### Sample 5

*Input:*
7  
4 1 2  
2 3 4  
6 5 6  
1 -1 -1  
3 -1 -1  
5 -1 -1  
7 -1 -1  

*Output:*  
CORRECT  

**Explanation:**
        4
       / \
      /   \
     2     6
    / \   / \
   1   3 5   7

This is a full binary tree, and the property of the binary search tree is satisfied in every node.

#### Sample 6

*Input:*  
4  
4 1 -1  
2 2 3  
1 -1 -1  
5 -1 -1  

*Output:*
INCORRECT  

**Explanation:**  
        4
       /
      2
     / \
    1   5

Node 5 is in the left subtree of the root, but it is bigger than the key 4 in the root.

#### What to Do
Testing the binary search tree condition for each node and every other node in its subtree will be too slow. You should come up with a faster algorithm.

#### Implementation in Python

[6-2_is_binary_search_tree.py](6-2_is_binary_search_tree.py)

'''
