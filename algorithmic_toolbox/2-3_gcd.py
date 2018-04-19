# Uses python3

import argparse
import datetime
import random
import sys

def gcdFast(a, b):

    rest = None

    my_a = max(a, b)
    my_b = min(a, b)

    while(rest != 0):
        rest = my_a % my_b
        my_a = my_b
        my_b = rest

    return my_a


def gcdNaive(a, b):

    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-01'

    parser = argparse.ArgumentParser(description='calculate the greatest common devisor (gcd)',
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

            a = random.randint(1, 2000000000)
            b = random.randint(1, 2000000000)

            print(str(a) + ' ' + str(b))

            current_time1 = datetime.datetime.now()
            res1 = gcdNaive(a, b)

            current_time2 = datetime.datetime.now()
            res2 = gcdFast(a, b)

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
        print(gcdFast(a, b))

    elif args.naive:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(gcdNaive(a, b))


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        a, b = map(int, input.split())
        print(gcdFast(a, b))



# original programming assignment

'''
### 2.3 Greatest Common Divisor

#### Problem Introduction
The greatest common divisor GCD(a, b) of two non-negative integers a and b (which are not both equal to 0) is the greatest integer d that divides both a and b. Your goal in this problem is to implement the Euclidean algorithm for computing
the greatest common divisor.
Efficient algorithm for computing the greatest common divisor is an important basic primitive of commonly used cryptographic algorithms like RSA.

#### Problem Description
**Task:** Given two integers a and b, find their greatest common divisor.
**Input Format:** The two integers a, b are given in the same line separated by space.
**Constraints:** 1 ≤ a, b ≤ 2 · 10^9 .
**Output Format:** Output GCD(a, b).

#### Sample 1

*Input*:
18 35

*Output*:
1
18 and 35 do not have common non-trivial divisors.

#### Sample 2

*Input*:
28851538 1183019

*Output*:
17657
28851538 = 17657 · 1634, 1183019 = 17657 · 67.

#### Implementation in Python

'''
