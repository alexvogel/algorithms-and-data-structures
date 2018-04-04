# Uses python3
import argparse
import random
import sys
import datetime
import string


def knapsack_dynamic_programming(capacity, bars, solutiontable=False):

    n = len(bars)

    # create the matrix
    # rows => gold_bars, columns => weight
    matrix = [[None] * (capacity+1) for i in range(n+1)]

    # initialize all values in row 0 with 0
    matrix[0] = [0] * len(matrix[0])

    # initialize all values in column 0 with 0
    for i in range(0, len(matrix)):
        matrix[i][0] = 0

    for i in range(1, n+1):
        for w in range(1, capacity+1):

            matrix[i][w] = matrix[i-1][w]

            if bars[i-1] <= w:
                val = matrix[i-1][w-bars[i-1]] + bars[i-1]

                # if existent value of cell is smaller, use the new value
                if matrix[i][w] < val:
                    matrix[i][w] = val

    if solutiontable:
        for row in matrix:
            print(row)

    return matrix[n][capacity]

def knapsack_greedy(W, w):

    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-04'

    parser = argparse.ArgumentParser(description='knapsack without repetitions and without fractions',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--solutiontable', action='store_true',
                       help='print the solution table along with the result')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            capacity = random.randint(10, 20)

            amount_gold_bars = random.randint(capacity//5, capacity//2)

            print(str(capacity) + ' ' + str(amount_gold_bars))

            gold_bars = []

            for gold_bar in range(0, amount_gold_bars):

                # print('min size: ' + str(capacity//8))
                # print('max size: ' + str(capacity//3))

                size_gold_bar = random.randint(capacity//8, capacity//3)
                gold_bars.append(size_gold_bar)

            for gold_bar in gold_bars:
                print(gold_bar, end=' ')

            print()

            current_time1 = datetime.datetime.now()
            maxweight = knapsack_dynamic_programming(capacity, gold_bars, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(maxweight))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        W, n, *w = list(map(int, input.split()))
        if args.solutiontable:
            print(knapsack_dynamic_programming(W, w, solutiontable=True))
        else:
            print(knapsack_dynamic_programming(W, w, solutiontable=False))
