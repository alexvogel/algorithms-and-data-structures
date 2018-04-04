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
