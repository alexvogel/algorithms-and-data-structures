# Uses python3
import argparse
import random
import sys
import datetime
import string


class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def SetData(self, n, data):
    self._data = data
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])


  # to build a max-heap use type='max' or taype='min' for a min-heap
  def buildHeap(self, heaptype='max'):
    maxIndex = len(self._data) - 1

    for i in reversed(range(0, (maxIndex//2)+1)):
        self._SiftDown(i, heaptype=heaptype)

  def _Parent(self, i):
    return (i-1) // 2

  def _LeftChild(self, i):
    return 2*i + 1

  def _RightChild(self, i):
    return 2*i + 2

  def _SiftUp(self, i, heaptype='max'):
    
    if heaptype == 'max':
        while i > 1 and self._data[self._Parent(i)] < self._data[i]:

            j = self._Parent(i)

            self._swaps.append((i, j))
            self._data[i], self._data[j] = self._data[j], self._data[i]

            i = self._Parent(i)
    elif heaptype == 'min':
        while i > 1 and self._data[self._Parent(i)] > self._data[i]:

            j = self._Parent(i)

            self._swaps.append((i, j))
            self._data[i], self._data[j] = self._data[j], self._data[i]

            i = self._Parent(i)


  def _SiftDown(self, i, heaptype='max'):

    maxIndex = i

    l = self._LeftChild(i)

    if l < len(self._data):

        if heaptype == 'max':
            if self._data[l] > self._data[maxIndex]:
                maxIndex = l
        elif heaptype == 'min':
            if self._data[l] < self._data[maxIndex]:
                maxIndex = l

    r = self._RightChild(i)

    if r < len(self._data):
        if heaptype == 'max':
            if self._data[r] > self._data[maxIndex]:
                maxIndex = r
        elif heaptype == 'min':
            if self._data[r] < self._data[maxIndex]:
                maxIndex = r


    if i != maxIndex:
        self._swaps.append((i, maxIndex))
        self._data[i], self._data[maxIndex] = self._data[maxIndex], self._data[i]

        self._SiftDown(maxIndex, heaptype=heaptype)

  def printHeap(self):
    print(self._data)


if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-17'

    parser = argparse.ArgumentParser(description='create a heap from an array',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--printheap', action='store_true',
                       help='print the heap array along with the result')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(4, 10)

            print(n)

            a = []

            for i in range(0, n):

                a_i = None

                while a_i == None or a_i in a:
                    a_i = random.randint(1, 1000)

                a.append(a_i)

            for a_i in a:
                print(a_i, end=' ')

            print()

            current_time1 = datetime.datetime.now()
            heap_builder = HeapBuilder()
            heap_builder.SetData(n, a)
            heap_builder.buildHeap(heaptype='min')
            heap_builder.WriteResponse()
            current_time2 = datetime.datetime.now()
            
            if args.printheap:
                heap_builder.printHeap()
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        heap_builder = HeapBuilder()
        heap_builder.ReadData()
        heap_builder.buildHeap(heaptype='min')
        heap_builder.WriteResponse()
        if args.printheap:
            heap_builder.printHeap()



# original programming assignment

'''
### 3.1 Convert Array Into Heap

#### Problem Introduction
In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting algorithm called HeapSort. It has guaranteed worst-case running time of O(n log n) as opposed to QuickSort’s average running time of O(n log n). QuickSort is usually used in practice, because typically it is faster, but HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your
computer.

#### Problem Description
**Task:** The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the way, did you know that algorithms based on Heaps are widely used for external sort, when you need to sort huge files that don’t fit into memory of a computer? Your task is to implement this first step and convert a given array of integers into a heap. You will do that by applying a certain number of swaps to the array. Swap is an operation which exchanges elements a i and a j of the array a for some i and j. You will need to convert the array into a heap using only O(n) swaps, as was described in the lectures. Note that you will need to use a min-heap instead of a max-heap in this problem.
**Input Format:** The first line of the input contains single integer n. The next line contains n space-separated integers a_i .
**Constraints:** 1 ≤ n ≤ 100000; 0 ≤ i, j ≤ n − 1; 0 ≤ a_0 , a_1 , . . . , a_n−1 ≤ 10^9 . All a_i are distinct.
**Output Format:** The first line of the output should contain single integer m — the total number of swaps. m must satisfy conditions 0 ≤ m ≤ 4n. The next m lines should contain the swap operations used to convert the array a into a heap. Each swap is described by a pair of integers i, j — the 0-based indices of the elements to be swapped. After applying all the swaps in the specified order the array must become a heap, that is, for each i where 0 ≤ i ≤ n − 1 the following conditions must be true:
1. If 2i + 1 ≤ n − 1, then a_i < a_2i+1 .
2. If 2i + 2 ≤ n − 1, then a_i < a_2i+2 .
Note that all the elements of the input array are distinct. Note that any sequence of swaps that has length at most 4n and after which your initial array becomes a correct heap will be graded as correct.
**Time Limits:** C: 1 sec, C++: 1 sec, Java: 3 sec, Python: 3 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript: 3 sec, Ruby: 3 sec, Scala: 3 sec.
**Memory Limit:** 512Mb.

#### Sample 1

*Input:*
5
5 4 3 2 1

*Output:*
3
1 4
0 1
1 3
**Explanation:**
After swapping elements 4 in position 1 and 1 in position 4 the array becomes 5 1 3 2 4.
After swapping elements 5 in position 0 and 1 in position 1 the array becomes 1 5 3 2 4.
After swapping elements 5 in position 1 and 2 in position 3 the array becomes 1 2 3 5 4, which is already a heap, because a_0 = 1 < 2 = a_1 , a_0 = 1 < 3 = a_2 , a_1 = 2 < 5 = a_3 , a_1 = 2 < 4 = a_4 .

#### Sample 2

*Input:*
5
1 2 3 4 5

*Output:*
0
**Explanation:**
The input array is already a heap, because it is sorted in increasing order.

What to Do
Implement the BuildHeap algorithm and account for min-heap instead of max-heap and for 0-based indexing.

#### Implementation in Python

'''
