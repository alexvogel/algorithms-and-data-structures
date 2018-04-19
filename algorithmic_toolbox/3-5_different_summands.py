# Uses python3
import argparse
import random
import sys
import datetime
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_summands(n):
    summands = []
    
    rest = n

    while(rest > 0):

        if len(summands) > 0:
            if rest > summands[-1]:
                last_summand = summands[-1]
                summands.append(last_summand+1)
                rest -= (last_summand+1)

            else:
                summands[-1] += rest
                rest = 0

        else:
            summands.append(1)
            rest -= 1

        #print('rest=' + str(rest))

    return summands


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-13'

    parser = argparse.ArgumentParser(description='different summands',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 1000)
            print(n)

            current_time1 = datetime.datetime.now()
            summands = optimal_summands(n)
            current_time2 = datetime.datetime.now()

            print(len(summands))
            for s in summands:
                print(s, end=' ')
            
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        n = int(input)
        summands = optimal_summands(n)
        print(len(summands))
        for x in summands:
            print(x, end=' ')



# original programming assignment

'''
### 3.5 Maximum Number of Prizes

#### Problem Introduction
You are organizing a funny competition for children. As a prize fund you have n candies. You would like to use these candies for top k places in a competition with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest value of k for which it is possible.

#### Problem Description
**Task:** The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum k such that n can be written as
a_1 + a_2 + · · · + a_k where a_1 , . . . , a_k are positive integers and a_i != a_j for all 1 ≤ i < j ≤ k.
**Input Format:** The input consists of a single integer n.
**Constraints:** 1 ≤ n ≤ 10^9 .
**Output Format:** In the first line, output the maximum number k such that n can be represented as a sum
of k pairwise distinct positive integers. In the second line, output k pairwise distinct positive integers
that sum up to n (if there are many such representations, output any of them).

#### Sample 1

*Input:*
6

*Output:*
3
1 2 3

#### Sample 2

*Input:*
8

*Output:*
3
1 2 5

#### Sample 3

*Input:*
2

*Output:*
1
2

#### Implementation in Python

'''
