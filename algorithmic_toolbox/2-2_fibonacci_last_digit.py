# Uses python3

import argparse
import datetime
import random

def calcFibonacciLastDigitFast(n):

    fibonacciLastDigit = [0, 1]

    if n>1:
        for i in range(2,n+1):
            #print('i=' + str(i))
            fibonacciLastDigit.append( (fibonacciLastDigit[i-1] + fibonacciLastDigit[i-2]) % 10)

    return fibonacciLastDigit[n]

def calcFibonacciLastDigitNaive(n):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-01'

    parser = argparse.ArgumentParser(description='calculate the last digit of a fibonacci number',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='to perform a stress test')
    parser.add_argument('--fast', action='store_true',
                       help='to use the fast algorithm')
    parser.add_argument('--naive', action='store_true',
                       help='to use the naive algorithm')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(0, 500000)

            print(n)

            current_time1 = datetime.datetime.now()
            res1 = calcFibonacciLastDigitNaive(n)

            current_time2 = datetime.datetime.now()
            res2 = calcFibonacciLastDigitFast(n)

            current_time3 = datetime.datetime.now()

            if(res1 != res2):
                print("Wrong answer: " + str(res1) + ' ' + str(res2))
                break
            else:
                print('OK:' + str(res1))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')

    elif args.fast:
        n = int(input())
        print(calcFibonacciLastDigitFast(n))

    elif args.naive:
        n = int(input())
        print(calcFibonacciLastDigitNaive(n))


    # this is called when no arguments are used
    else:
        n = int(input())
        print(calcFibonacciLastDigitFast(n))



# original programming assignment

'''
### 2.2 Last Digit of a Large Fibonacci Number

#### Problem Introduction
Your goal in this problem is to find the last digit of n-th Fibonacci number. Recall that Fibonacci numbers grow exponentially fast. For example,
F_200 = 280571172992510140037611932413038677189525 .
Therefore, a solution like

 ```
F[0] ← 0
F[1] ← 1
for i from 2 to n:
F[i] ← F[i − 1] + F[i − 2]
print(F[n] mod 10)
```

will turn out to be too slow, because as i grows the ith iteration of the loop computes the sum of longer and longer numbers. Also, for example, F_1000 does not fit into the standard C++ int type. To overcome this difficulty, you may want to store in F [i] not the ith Fibonacci number itself, but just its last digit (that is, F_i mod 10). Computing the last digit of F_i is easy: it is just the last digit of the sum of the last digits of
F_i−1 and F_i−2 :
F[i] ← (F[i − 1] + F[i − 2]) mod 10
This way, all F[i]’s are just digits, so they fit perfectly into any standard integer type, and computing a sum
of F[i − 1] and F[i − 2] is performed very quickly.

#### Problem Description
**Task:** Given an integer n, find the last digit of the nth Fibonacci number F_n (that is, F_n mod 10).
**Input Format:** The input consists of a single integer n.
**Constraints:** 0 ≤ n ≤ 10^7 .
**Output Format:** Output the last digit of F_n .

#### Sample 1

*Input*:
3

*Output*:
2
F_3 = 2.

#### Sample 2

*Input*:
331

*Output*:
9
F_331 = 668996615388005031531000081241745415306766517246774551964595292186469.

#### Implementation in Python

'''
