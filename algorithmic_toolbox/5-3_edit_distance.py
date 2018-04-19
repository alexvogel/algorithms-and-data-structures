# Uses python3
import argparse
import random
import sys
import datetime
import string
import pandas as pd

def edit_distance(s, t, solutiontable=False):

    len_s = len(s) + 1
    len_t = len(t) + 1

    # create distance matrix
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):

            # if corresponding characters are equal
            if s[i - 1] == t[j - 1]:
                # use the value from the diagonal neighbor cell
                d[i][j] = d[i - 1][j - 1]

                # use the minimum value from all neighbor cells and add 1
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    if solutiontable:
        print('solutiontable:')
        for i in range(0, len(d)):
            print(d[i])

    # the value in the lower right corner is the edit distance
    return d[-1][-1]

def edit_distance_pandas(s, t, solutiontable=False):

    # create a pandas dataframe as the distance matrix
    # amount of columns == len(t)+1
    # amount of rows == len(s)+1
    df = pd.DataFrame(index=range(-1, len(s) + 1), columns=range(-1, len(t) + 1))

    # put in the characters of the two words into the distance matrix
    # string s in column '-1' (i is the id of row)
    for i in range(0, len(s)):
        df.set_value(i+1, -1, s[i])

    # string t in row '-1' (j is the id of column)
    for j in range(0, len(t)):
        df.set_value(-1, j+1, t[j])

    # set the corner to 0
    df.set_value(0, 0, 0)

    # set the first column values
    for i in range(0, len(s) + 1):
        df.set_value(i, 0, i)

    # set the first row values
    for j in range(0, len(t) + 1):
        df.set_value(0, j, j)

    # debug
#    print(df)

    # fill the solution table
    for i in range(1, len(s) + 1):      # for each row
        for j in range(1, len(t) + 1):  # for each column

            # if characters are equal, then take the number of edits from the diagonal neighbor
            if df.loc[i, -1] == df.loc[-1, j]:
                df.set_value(i, j, df.loc[i-1, j-1])

            #elif df.loc[i, -1] != df.loc[-1, j]:
            else:
                # the minimum of neighbor cells plus 1
                df.set_value(i, j, 1 + min( (df.loc[i-1, j-1], df.loc[i-1, j], df.loc[i, j-1]) ))

    if solutiontable:
        print('solutiontable:')
        print(df)

    # return the edit distance. this is the value in the right lower corner of the table
    return df.iloc[-1, -1]

if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-31'

    parser = argparse.ArgumentParser(description='dynamic programming - edit distance',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--solutiontable', action='store_true',
                       help='print the solution table along with the result')
    parser.add_argument('--pandas', action='store_true',
                       help='solution with use of the pandas module')
    parser.add_argument('--standard', action='store_true',
                       help='solution with standard lists (without pandas)')

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
            amount_coins = edit_distance(string_1, string_2, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(amount_coins))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    elif args.pandas:
        if args.solutiontable:
            print(edit_distance_pandas(input(), input(), solutiontable=True))
        else:
            print(edit_distance_pandas(input(), input()))

    elif args.standard:
        if args.solutiontable:
            print(edit_distance(input(), input(), solutiontable=True))
        else:
            print(edit_distance(input(), input()))

    # this is called when no arguments are used
    else:
        if args.solutiontable:
            print(edit_distance(input(), input(), solutiontable=True))
        else:
            print(edit_distance(input(), input()))



# original programming assignment

'''
### 5.3 Edit Distance

#### Problem Introduction
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, in computational biology, natural language processing, and spell checking. Your goal in this problem is to compute the edit distance between two strings.

#### Problem Description
**Task:** The goal of this problem is to implement the algorithm for computing the edit distance between two strings.
**Input Format:** Each of the two lines of the input contains a string consisting of lower case latin letters.
**Constraints:** The length of both strings is at least 1 and at most 100.
**Output Format:** Output the edit distance between the given two strings.

#### Sample 1

*Input:*
ab
ab

*Output:*
0

#### Sample 2

*Input:*
short
ports

*Output:*
3
An alignment of total cost 3:
```
s h o r t −
− p o r t s
```

#### Sample 3

*Input:*
editing
distance

*Output:*
5
An alignment of total cost 5:
```
e d i − t i n g −
− d i s t a n c e
```

#### Implementation in Python

'''
