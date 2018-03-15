# Uses python3
import argparse
import random
import sys
import datetime
from collections import namedtuple

def getGreaterOrEqual(digit, maxDigit):

    a = str(digit) + str(maxDigit)
    b = str(maxDigit) + str(digit)

    if a > b:
        return digit
    else:
        return maxDigit

def largest_number(a):
    #write your code here
    res = ''

    while(len(a) > 0):
        maxDigit = -9999

        for digit in a:

            maxDigit = getGreaterOrEqual(digit, maxDigit)

        res += maxDigit

        #print('remove digit ' + str(maxDigit) + ' from list ' + str(a))
        a.remove(str(maxDigit))


    return res


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

            n = random.randint(1, 10)
            print(n)

            numbers = []
            for i in range(1, n):
                numbers.append(str(random.randint(1, 1000)))

            for number in numbers:
                print(number, end=' ')
            print("\n")

            current_time1 = datetime.datetime.now()
            res = largest_number(numbers)
            current_time2 = datetime.datetime.now()

            print(res)
            
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = input.split()
        a = data[1:]
        print(largest_number(a))
