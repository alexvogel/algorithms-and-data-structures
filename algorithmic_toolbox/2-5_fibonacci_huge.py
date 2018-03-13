# Uses python3

import argparse
import datetime
import random
import sys
from fractions import Fraction

# function for detecting the Pisano Period for given m
def detectPisanoPeriod(m):
    a = 0
    b = 1
    c = a+b

    for i in range(0, m*m):
        c = (a + b) % m
        a = b
        b = c

        if((a == 0) and (b == 1)):
            return i + 1


def detectPisanoPeriodOld(m):

    possible_second_seq_start = None
    confirmed_second_seq_start = None

    n = -1

    seq = []

    while(True):

        n += 1

        res = calcFibonacciNumberFast(n) % m

        #print('n=' + str(n) + ': res=' + str(res))

        seq.append(res)

        if n>0:

            if possible_second_seq_start == None:

                if res == seq[0]:
                    possible_second_seq_start = n
                    #print(str(n) + ': (Fn_mod_' + str(m) + '=' + str(res) + '): possible second sequence start')

            elif possible_second_seq_start != None:

                # if Fibonacci of n equals previous Fibonacci
                if res == seq[n - possible_second_seq_start]:
                    #print(str(n) + ': (Fn_mod_' + str(m) + '=' + str(res) + '): confirmation on sequence')
                    confirmed_second_seq_start = possible_second_seq_start

                    if (n+1) % (possible_second_seq_start) == 0:
                        #print('sequence fully confirmed')
                        return confirmed_second_seq_start

                # otherwise
                else:
                    #print(str(n) + ': (Fn_mod_' + str(m) + '=' + str(res) + '): false alarm. resetting possible_sequence_start')
                    possible_second_seq_start = None


def calcFibonacciNumberFast(n):

    fibonacci = [0, 1]

    if n>1:
        for i in range(2,n+1):
            #print('i=' + str(i))
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    return fibonacci[n]

# this is the fast implementation
def fibonacciHugeFast(n, m):

    lengthPisanoPeriod = detectPisanoPeriod(m)

    #print('sequence is: ' + str(seq))

    remainder = n % (lengthPisanoPeriod)

    fib = calcFibonacciNumberFast(remainder)

    return (fib % m)


# this is the obvious/naive implementation
def fibonacciHugeNaive(n, m):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-03'

    parser = argparse.ArgumentParser(description='calculate the modulo of a huge fibonacci number',
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

            n = random.randint(1, 2000)
            m = random.randint(2, 200)

            print(str(n) + ' ' + str(m))

            current_time1 = datetime.datetime.now()
            res1 = fibonacciHugeNaive(n, m)

            current_time2 = datetime.datetime.now()
            res2 = fibonacciHugeFast(n, m)

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
        n, m = map(int, input.split())
        print(fibonacciHugeFast(n, m))

    elif args.naive:
        input = sys.stdin.read();
        n, m = map(int, input.split())
        print(fibonacciHugeNaive(n, m))


    # this is called when no arguments are used
    else:
        input = sys.stdin.read();
        n, m = map(int, input.split())
        print(fibonacciHugeFast(n, m))
