# Uses python3

import argparse
import random

def maxPairwiseProductFast(numbers):

    result = 0

    numbers = list(reversed(sorted(numbers)))
    
    return numbers[0] * numbers[1]

def maxPairwiseProduct(numbers):

    result = 0

    for i in range(len(numbers)):

        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > result:
                result = numbers[i] * numbers[j]

    return result

if __name__ == '__main__':

    version = '0.1'
    date = '2018-02-28'

    parser = argparse.ArgumentParser(description='algorithms and data structures: maximum pairwise product',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='to perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(2, 10)
            a = []

            for i in range (n):

                a.append(random.randint(0, 10))

            print(a)

            res1 = maxPairwiseProduct(a)
            res2 = maxPairwiseProductFast(a)

            if(res1 != res2):
                print("Wrong answer: " + str(res1) + ' ' + str(res2))
                break
            else:
                print('OK')

            print('------')

    else:

        n = int(input())
        a = [int(x) for x in input().split()]
        assert(len(a) == n)

        print(maxPairwiseProductFast(a))
