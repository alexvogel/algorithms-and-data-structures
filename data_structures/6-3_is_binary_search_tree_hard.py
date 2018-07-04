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

  if tree[index][0] < lowerBound or tree[index][0] >= upperBound:
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
