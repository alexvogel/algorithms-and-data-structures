# Uses python3
import argparse
import random
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.

    while(capacity > 0 and sum([a*b for a,b in zip(weights, values)]) > 0 ):

        #print('capacity: ' + str(capacity))

        index_max_value_per_unit = None
        max_value_per_unit = 0
        for i in range(0, len(weights)):

            #print(str(i) + ' weight: ' + str(weights[i]) + ' value: ' + str(values[i]))

            if weights[i] == 0:
                pass

            else:
                value_per_unit = values[i] / weights[i]

                if value_per_unit > max_value_per_unit:
                    max_value_per_unit = value_per_unit
                    index_max_value_per_unit = i

        #print('max value per unit brings item nr ' + str(index_max_value_per_unit))

        toLoot = min(capacity, weights[index_max_value_per_unit])

        value += toLoot/weights[index_max_value_per_unit] * values[index_max_value_per_unit]
        #print('item ' + str(index_max_value_per_unit) + ' pack in ' + str(toLoot) + ' kg of value ' + str(toLoot/weights[index_max_value_per_unit] * values[index_max_value_per_unit]) )
        #print('totals to ' + str(value))


        values[index_max_value_per_unit] = values[index_max_value_per_unit] * (1 - toLoot/weights[index_max_value_per_unit])
        weights[index_max_value_per_unit] = weights[index_max_value_per_unit] * (1 - toLoot/weights[index_max_value_per_unit])
        capacity -= toLoot

    return value


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-05'

    parser = argparse.ArgumentParser(description='calculate the optimal value - fractional knapsack problem with repetitions',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            capacity = random.randint(0, 1000)
            n = random.randint(1, 4)
            print(str(n) + ' ' + str(capacity))

            weights = []
            values = []

            for i in range(0, n):
                randomValue = random.randint(0, 20)
                randomWeight = random.randint(0, 20)
                values.append(randomValue)
                weights.append(randomWeight)

                print(str(randomValue) + ' ' + str(randomWeight))

            res = get_optimal_value(capacity, weights, values)

            print(res)
            print('------')

    # this is called when no arguments are used
    else:
        data = list(map(int, sys.stdin.read().split()))
        n, capacity = data[0:2]
        values = data[2:(2 * n + 2):2]
        weights = data[3:(2 * n + 2):2]
        opt_value = get_optimal_value(capacity, weights, values)
        print("{:.10f}".format(opt_value))



# original programming assignment

'''
### 3.2 Maximum Value of the Loot

#### Problem Introduction
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.

#### Problem Description
**Task:** The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
**Input Format:** The first line of the input contains the number n of items and the capacity W of a knapsack.
The next n lines define the values and weights of the items. The i-th line contains integers v i and w i —the
value and the weight of i-th item, respectively.
**Constraints:** 1 ≤ n ≤ 10^3 , 0 ≤ W ≤ 2 · 10^6 ; 0 ≤ v_i ≤ 2 · 10^6 , 0 < w_i ≤ 2 · 10^6 for all 1 ≤ i ≤ n. All the
numbers are integers.
**Output Format:** Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10^−3 . To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

#### Sample 1

*Input:*
3 50
60 20
100 50
120 30

*Output:*
180.0000
To achieve the value 180, we take the first item and the third item into the bag.

#### Sample 2

*Input:*
1 10
500 30

*Output:*
166.6667
Here, we just take one third of the only available item.

#### Implementation in Python

'''
