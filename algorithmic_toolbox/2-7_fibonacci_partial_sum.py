# Uses python3

import argparse
import datetime
import random
import sys
#from fractions import Fraction


# def fib(n):

#     if n <= 1:
#         return n

#     previous, current = 0, 1

#     for _ in range(2, n + 1):
#         previous, current = current, previous + current

#     return current


# def fibonacci_partial_sum_fast(from_, to):
#     a = from_ % 60
#     b = to % 60

#     res = 0
#     for i in range(a, b + 1):
#         res += fib(i)

#     return res % 10


# this is the fast implementation
def fibonacci_partial_sum_fast(from_, to):

    # mod 60 from lower bound
    a = from_ % 60

    # mod 60 from upper bound
    b = to % 60

    # initialize result
    result = 0

    lower = min(a, b)
    upper = max(a, b)

    #print('a=' + str(a) + '   b=' + str(b) )
    #print('lower=' + str(lower) + '   upper=' + str(upper) )

    for i in range(lower, upper +1):
        #print('i=' + str(i))

        if i <= 1:
            result += i

        else:
            prev = 0
            curr = 1

            for j in range(2, i+1):
                prev, curr = curr, prev + curr

            result += curr

    return result % 10


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


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

            rand_1 = random.randint(0, 100)
            rand_2 = random.randint(0, 100)

            m = min(rand_1, rand_2)
            n = max(rand_1, rand_2)

            print(str(m) + ' ' + str(n))

            current_time1 = datetime.datetime.now()
            res1 = fibonacci_partial_sum_naive(m, n)

            current_time2 = datetime.datetime.now()
            res2 = fibonacci_partial_sum_fast(m, n)

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
        from_, to = map(int, input.split())
        print(fibonacci_partial_sum_fast(from_, to))

    elif args.naive:
        input = sys.stdin.read();
        from_, to = map(int, input.split())
        print(fibonacci_partial_sum_naive(from_, to))


    # this is called when no arguments are used
    else:
        input = sys.stdin.read();
        from_, to = map(int, input.split())
        print(fibonacci_partial_sum_fast(from_, to))



# original programming assignment

'''
### 2.7 Last Digit of the Sum of Fibonacci Numbers Again

#### Problem Introduction
Now, we would like to find the last digit of a partial sum of Fibonacci numbers: F m + F m+1 + · · · + F n .

#### Problem Description
**Task:** Given two non-negative integers m and n, where m ≤ n, find the last digit of the sum F_m + F_m+1 +
· · · + F_n .
**Input Format:** The input consists of two non-negative integers m and n separated by a space.
**Constraints:** 0 ≤ m ≤ n ≤ 10^18 .
**Output Format:** Output the last digit of F_m + F_m+1 + · · · + F_n .

#### Sample 1

*Input:*
37

*Output:*
1
F_3 + F_4 + F_5 + F_6 + F_7 = 2 + 3 + 5 + 8 + 13 = 31.

#### Sample 2

*Input:*
10 10

*Output:*
5
F_10 = 55.

#### Sample 3

*Input:*
10 200

*Output:*
2
F_10 + F_11 + · · · + F_200 = 734544867157818093234908902110449296423262

#### Implementation in Python

'''
