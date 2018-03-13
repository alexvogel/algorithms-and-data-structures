# Uses python3
import argparse
import random
import sys
import datetime

def max_dot_product(a, b):
    #write your code here

    a = list(sorted(a))
    b = list(sorted(b))

    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-06'

    parser = argparse.ArgumentParser(description='calculate the maximal dotproduct',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 1000)

            print(n)

            a = []
            b = []

            for i in range(0, n):
                random_a = random.randint(-100000, +100000)
                random_b = random.randint(-100000, +100000)
                a.append(random_a)
                b.append(random_b)

            print(' '.join(map(str, a)))
            print(' '.join(map(str, b)))

            current_time1 = datetime.datetime.now()
            res = max_dot_product(a, b)
            current_time2 = datetime.datetime.now()

            print(str(res) + ' (runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        a = data[1:(n + 1)]
        b = data[(n + 1):]
        print(max_dot_product(a, b))
