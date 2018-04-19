# Uses python3
import argparse
import random
import sys
import datetime
import string

def lcs2(a, b, solutiontable=False):

    len_a = len(a)
    len_b = len(b)

    # create the subsequence matrix
    d = [[None] * (len_b + 1) for i in range(len_a + 1)]

    for i in range(len_a + 1):
        for j in range(len_b + 1):

            if i == 0 or j == 0:
                d[i][j] = 0

            elif a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1] + 1

            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])

    if solutiontable:
        for row in d:
            print(row)

    #d[len_a][len_b] contains the length of LCS of a[0..len_a-1] & b[0..len_b-1]
    return d[len_a][len_b]



if __name__ == "__main__":

    version = '0.1'
    date = '2018-04-04'

    parser = argparse.ArgumentParser(description='longest common subsequence of two sequences',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--solutiontable', action='store_true',
                       help='print the solution table along with the result')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            length_string_1 = random.randint(3, 10)
            length_string_2 = random.randint(length_string_1 - 1, length_string_1 + 1)
            
            string_1 = "".join(random.choice(string.ascii_letters) for x in range(length_string_1)).lower()
            string_2 = "".join(random.choice(string.ascii_letters) for x in range(length_string_2)).lower()

            print(string_1)
            print(string_2)

            current_time1 = datetime.datetime.now()
            lcs = lcs2(string_1, string_2, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(lcs))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))

        n = data[0]
        data = data[1:]
        a = data[:n]

        data = data[n:]
        m = data[0]
        data = data[1:]
        b = data[:m]

        if args.solutiontable:
            print(lcs2(a, b, solutiontable=True))
        else:
            print(lcs2(a, b))



# original programming assignment

'''
### 5.4 Longest Common Subsequence of Two Sequences

#### Problem Introduction
Compute the length of a longest common subsequence of three sequences.

#### Problem Description
**Task:** Given two sequences A = (a_1 , a_2 , . . . , a_n ) and B = (b_1 , b_2 , . . . , b_m ), find the length of their longest
common subsequence, i.e., the largest non-negative integer p such that there exist indices 1 ≤ i_1 < i_2 < · · · < i_p ≤ n and 1 ≤ j_1 < j_2 < · · · < j_p ≤ m, such that a_i_1 = b_j_1 , . . . , a_i_p = b_j_p .
**Input Format:** First line: n. Second line: a_1 , a_2 , . . . , a_n . Third line: m. Fourth line: b_1 , b_2 , . . . , b_m .
**Constraints:** 1 ≤ n, m ≤ 100; −10^9 < a_i , b_i < 10^9 .
**Output Format:** Output p.

#### Sample 1

*Input:*
3
2 7 5
2
2 5

*Output:*
2
A common subsequence of length 2 is (2, 5).

#### Sample 2

*Input:*
1
7
4
1 2 3 4

*Output:*
0
The two sequences do not share elements.

#### Sample 3

*Input:*
4
2 7 8 3
4
5 2 8 7

*Output:*
2
One common subsequence is (2, 7). Another one is (2, 8).

#### Implementation in Python

'''
