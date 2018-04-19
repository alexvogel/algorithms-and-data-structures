# Uses python3

import argparse
import random

def maxPairwiseProductFast(numbers):

    result = 0

    numbers = list(reversed(sorted(numbers)))
    
    return numbers[0] * numbers[1]

def maxPairwiseProductNaive(numbers):

    result = 0

    for i in range(len(numbers)):

        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > result:
                result = numbers[i] * numbers[j]

    return result

if __name__ == '__main__':

    version = '0.1'
    date = '2018-02-28'

    parser = argparse.ArgumentParser(description='algorithms and data structures: maximum pairwise product',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='to perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(2, 10)
            a = []

            for i in range (n):

                a.append(random.randint(0, 10))

            print(a)

            res1 = maxPairwiseProductNaive(a)
            res2 = maxPairwiseProductFast(a)

            if(res1 != res2):
                print("Wrong answer: " + str(res1) + ' ' + str(res2))
                break
            else:
                print('OK')

            print('------')

    else:

        n = int(input())
        a = [int(x) for x in input().split()]
        assert(len(a) == n)

        print(maxPairwiseProductFast(a))



# original programming assignment

'''
### 1.1 Maximum Pairwise Product Problem
**Task:** Find the maximum product of two distinct numbers in a sequence of non-negative integers.

**Input:**    A sequence of non-negative integers.
**Output:**   The maximum value that can be obtained by multiplying twi different elements from the sequence.

Given a sequence of non-negative integers a_1 , . . . , a_n , compute
max a_i · a_j .
1 ≤ i, j ≤ n
Note that i and j should be different, though it may be the case that a_i = a_j .
**Input format:** The first line contains an integer n. The next line contains
n non-negative integers a_1 , . . . , a_n (separated by spaces).
**Output format:** The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 10^5 ; 0 ≤ a_1 , . . . , a_n ≤ 2 · 10^5 .

#### Sample 1

*Input*:
3
1 2 3

*Output*:
6

#### Sample 2

*Input:*
10
7 5 14 2 8 8 10 1 2 3

*Output:*
140

#### Implementation in Python

'''
