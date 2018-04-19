# Uses python3

import argparse
import datetime
import random

def calcFibonacciNumberFast(n):

    fibonacci = [0, 1]

    if n>1:
        for i in range(2,n+1):
            #print('i=' + str(i))
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci[n]

def calcFibonacciNumberNaive(n):

    if (n <= 1):
        return n

    return calcFibonacciNumberNaive(n - 1) + calcFibonacciNumberNaive(n - 2)



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-01'

    parser = argparse.ArgumentParser(description='calculate fibonacci number',
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

            n = random.randint(2, 30)

            print(n)

            current_time1 = datetime.datetime.now()
            res1 = calcFibonacciNumberNaive(n)
            current_time2 = datetime.datetime.now()
            res2 = calcFibonacciNumberFast(n)
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

        print(calcFibonacciNumberFast(n))

    elif args.naive:
        n = int(input())

        print(calcFibonacciNumberNaive(n))


    # this is when called without any arguments
    else:

        n = int(input())

        print(calcFibonacciNumberFast(n))



# original programming assignment

'''
### 2.1 Fibonacci Number

#### Problem Introduction
The definition of Fibonacci sequence is: F_0 = 0, F_1 = 1, and F_i = F_i−1 + F_i−2 for i ≥ 2.

```
Fibonacci(n):
    if n ≤ 1:
        return n
    return Fibonacci(n − 1) + Fibonacci(n − 2)
```

The input consists of a single integer n.
**Constraints:** 0 ≤ n ≤ 45.
**Output Format:** Output F_n .

#### Sample 1

*Input*:
10

*Output*:
55
F_10 = 55.

#### Implementation in Python

'''
