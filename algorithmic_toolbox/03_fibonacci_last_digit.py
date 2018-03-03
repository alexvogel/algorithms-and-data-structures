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
