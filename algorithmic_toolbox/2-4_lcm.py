# Uses python3

import argparse
import datetime
import random
import sys
from fractions import Fraction

# helper function for the lcmFast algorithm
def gcdFast(a, b):

    rest = None

    my_a = max(a, b)
    my_b = min(a, b)

    while(rest != 0):
        rest = my_a % my_b
        my_a = my_b
        my_b = rest

    return my_a

# this is the fast implementation
def lcmFast(a, b):
    return int(Fraction(a*b, gcdFast(a, b)))

# this is the obvious/naive implementation
def lcmNaive(a, b):

    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-01'

    parser = argparse.ArgumentParser(description='calculate the least common multiple (gcd)',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--fast', action='store_true',
                       help='use the fast algorithm')
    parser.add_argument('--naive', action='store_true',
                       help='use the naive algorithm')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            a = random.randint(1, 2000)
            b = random.randint(1, 2000)

            print(str(a) + ' ' + str(b))

            current_time1 = datetime.datetime.now()
            res1 = lcmNaive(a, b)

            current_time2 = datetime.datetime.now()
            res2 = lcmFast(a, b)

            current_time3 = datetime.datetime.now()

            if(res1 != res2):
                print("Wrong answer: " + str(res1) + ' ' + str(res2))
                break
            else:
                print('OK:' + str(res1))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')

    elif args.fast:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(lcmFast(a, b))

    elif args.naive:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(lcmNaive(a, b))


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(lcmFast(a, b))



# original programming assignment

'''
### 2.4 Least Common Multiple

#### Problem Introduction
The least common multiple of two positive integers a and b is the least positive integer m that is divisible by both a and b.

#### Problem Description
**Task:** Given two integers a and b, find their least common multiple.
**Input Format:** The two integers a and b are given in the same line separated by space.
**Constraints:** 1 ≤ a, b ≤ 2 · 10^9 .
**Output Format:** Output the least common multiple of a and b.

#### Sample 1

*Input*:
68

*Output*:
24
Among all the positive integers that are divisible by both 6 and 8 (e.g., 48, 480, 24), 24 is the smallest
one.

#### Sample 2

*Input*:
28851538 1183019

*Output*:
1933053046
1933053046 is the smallest positive integer divisible by both 28851538 and 1183019.

#### Implementation in Python

'''
