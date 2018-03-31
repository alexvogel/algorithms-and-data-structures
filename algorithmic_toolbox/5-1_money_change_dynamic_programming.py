# Uses python3
import argparse
import random
import sys
import datetime
import math

def get_change_dynamic_programming(money):
    
    # define possible denominations
    denominations = [1, 3, 4]

    # create a list for coincount
    T = [math.inf] * (money + 1)

    # the amount of coins for a total of 0 is also 0
    # this definition is important, because all other calculations base on this number
    T[0] = 0

    # create a list for the used coins
    R = [-1] * (money + 1)

    # loop over denominations
    for j in range(0, len(denominations)):
        for i in range(0, len(T)):
            if i >= denominations[j]:
                T[i] = min(T[i], 1 + T[i - denominations[j]])
                R[i] = j

    # print the used coins
    # start = len(R) - 1
    # while start != 0:

    #     j = R[start]
    #     print( denominations[j] )
    #     start = start - denominations[j]

    # the result is the amount of coins for the money
    return T[money]


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-30'

    parser = argparse.ArgumentParser(description='dynamic programming - money change again',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            money = random.randint(1, 1000)
            print(money)

            current_time1 = datetime.datetime.now()
            amount_coins = get_change_dynamic_programming(money)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(amount_coins))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        m = int(sys.stdin.read())
        print(get_change_dynamic_programming(m))
