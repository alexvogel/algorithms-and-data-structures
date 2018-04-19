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



# original programming assignment

'''
### 3.3 Maximum Advertisement Revenue

#### Problem Introduction
You have n ads to place on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up n slots on your page and estimated the expected number of clicks per day for each
slot. Now, your goal is to distribute the ads among the slots to maximize the total revenue.

#### Problem Description
**Task:** Given two sequences a_1 , a_2 , . . . , a_n (a_i is the profit per click of the i-th ad) and b_1 , b_2 , . . . , b_n (b_i is the average number of clicks per day of the i-th slot), we need to partition them into n pairs (a_i , b_j)
such that the sum of their products is maximized.
**Input Format:** The first line contains an integer n, the second one contains a sequence of integers
a_1, a_2 , . . . ,a_n , the third one contains a sequence of integers b_1 , b_2 , . . . , b_n .
**Constraints:** 1 ≤ n ≤ 10^3 ; −10^5 ≤ a_i , b_i ≤ 10^5 for all 1 ≤ i ≤ n.
**Output Format:** Output the maximum value of
n
∑︀a_i c_i , where c_1 , c_2 , . . . , c_n is a permutation of b_1 , b_2 , . . . , b_n.
i=1


#### Sample 1

*Input:*
1
23
39

*Output:*
897
897 = 23 · 39.

#### Sample 2

*Input:*
3
1 3 -5
-2 4 1

*Output:*
23
23 = 3 · 4 + 1 · 1 + (−5) · (−2).

#### Implementation in Python

'''
