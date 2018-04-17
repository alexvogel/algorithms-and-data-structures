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
