# Uses python3
import argparse
import random
import sys
import datetime
import string


def partition3(A, solutiontable=False):

    sum_A = 0
    len_A = len(A)

    # calc sum of elements
    for i in range(0, len_A):
        sum_A += A[i]

    # if sum is dividable by three, then it is possibly divideable in 3 partionable
    if (sum_A % 3 != 0):
        return 0

    # create matrix
    # amount of rows = sum_A/3 + 1
    # amount of columns = len_A + 1
    matrix = [[None] * (len_A+1) for i in range(sum_A//3+1)]

    # initialize all values in column 0 with False
    for i in range(0, len(matrix)):
        matrix[i][0] = False

    # initialize all values in row 0 with True (inclusive the cell 0,0)
    matrix[0] = [True] * len(matrix[0])

    # fill partition table bottom up
    for i in range(1, sum_A//3 + 1):
        for j in range(1, len_A + 1):
            matrix[i][j] = matrix[i][j-1]

            if i >= A[j-1]:
                matrix[i][j] = matrix[i][j] or matrix[i - A[j-1]][j-1]


    if solutiontable:
        for row in matrix:
            print(row)

    return int(matrix[sum_A//3][len_A])

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

            n = random.randint(4, 10)

            # print n as first line
            print(n)

            # souvenirs
            A = []

            for i in range(0, n):

                souvenir = random.randint(1, 10)
                A.append(souvenir)

            # print all souvenirs in one line
            for souvenir in A:
                print(souvenir, end=' ')

            # print newline
            print()

            # make timed call
            current_time1 = datetime.datetime.now()
            isPartitionPossible = partition3(A, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(isPartitionPossible))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        n, *A = list(map(int, input.split()))
#        print(partition3(A))
        if args.solutiontable:
            print(partition3(A, solutiontable=True))
        else:
            print(partition3(A, solutiontable=False))



# original programming assignment

'''
### 6.2 Partitioning Souvenirs

#### Problem Introduction
You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

#### Problem Description
**Input Format:** The first line contains an integer n. The second line contains integers v_1 , v_2 , . . . , v_n separated by spaces.
**Constraints:** 1 ≤ n ≤ 20, 1 ≤ v_i ≤ 30 for all i.
**Output Format:** Output 1, if it possible to partition v_1 , v_2 , . . . , v_n into three subsets with equal sums, and 0 otherwise.

#### Sample 1

*Input:*
4
3 3 3 3

*Output:*
0

#### Sample 2

*Input:*
1
40

*Output:*
0

#### Sample 3

*Input:*
11
17 59 34 57 17 23 67 1 18 2 59

*Output:*
1
34 + 67 + 17 = 23 + 59 + 1 + 17 + 18 = 59 + 2 + 57.

#### Sample 4

*Input:*
13
1 2 3 4 5 5 7 7 8 10 12 19 25

*Output:*
1
1 + 3 + 7 + 25 = 2 + 4 + 5 + 7 + 8 + 10 = 5 + 12 + 19.

#### Implementation in Python

'''
