# Uses python3

import argparse
import datetime
import random
import sys
#from fractions import Fraction


# this is the fast implementation
def fibonacci_sum_fast(n):

    m = (n+2) % 60

    # preinitialize list
    fibonacci = [None] * (m+1)

    fibonacci[0] = 0

    if(m == 0):
        fibonacci.append(1)
    else:
        fibonacci[1] = 1

    result = 1

    for i in range(2, m+1):
        fibonacci[i] = (fibonacci[i-1] % 10 + fibonacci[i-2] % 10) % 10

    if fibonacci[m] == 0:
        return 9

    return (fibonacci[m] % 10 -1)


# part of the naive solution
def fib(n):

    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current

# this is the obvious/naive implementation
def fibonacci_sum_naive(n):
    m = (n + 2) % 60
    return ((fib(m) - 1) % 10)


if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-13'

    parser = argparse.ArgumentParser(description='calculate the last digit of the sum of fibonacci numbers',
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

            n = random.randint(1, 20000000000000)

            print(str(n))

            current_time1 = datetime.datetime.now()
            res1 = fibonacci_sum_naive(n)

            current_time2 = datetime.datetime.now()
            res2 = fibonacci_sum_fast(n)

            current_time3 = datetime.datetime.now()

            if(res1 != res2):
                print("Wrong answer: " + str(res1) + ' ' + str(res2))
                break
            else:
                print('OK:' + str(res1))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')

    elif args.fast:
        input = sys.stdin.read();
        n = int(input)
        print(fibonacci_sum_fast(n))

    elif args.naive:
        input = sys.stdin.read();
        n = int(input)
        print(fibonacci_sum_naive(n))


    # this is called when no arguments are used
    else:
        input = sys.stdin.read();
        n = int(input)
        print(fibonacci_sum_fast(n))



# original programming assignment

'''
### 2.6 Last Digit of the Sum of Fibonacci Numbers

#### Problem Introduction
The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.

#### Problem Description
**Task:** Given an integer n, find the last digit of the sum F_0 + F_1 + · · · + F_n .
**Input Format:** The input consists of a single integer n.
**Constraints:** 0 ≤ n ≤ 10^14 .
**Output Format:** Output the last digit of F_0 + F_1 + · · · + F_n .

#### Sample 1

*Input*:
3

*Output:*
4
F_0 + F_1 + F_2 + F_3 = 0 + 1 + 1 + 2 = 4.

#### Sample 2

*Input*:
100

*Output:*
5
The sum is equal to 927372692193078999175, the last digit is 5.

#### What To Do
Instead of computing this sum in a loop, try to come up with a formula for F_0 + F_1 + F_2 + · · · + F_n . For   this, play with small values of n. Then, use a solution for the previous problem.

#### Implementation in Python

'''
