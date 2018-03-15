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
