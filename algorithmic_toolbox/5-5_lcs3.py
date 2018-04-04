# Uses python3
import argparse
import random
import sys
import datetime
import string

def lcs3(a, b, c, solutiontable=False):

    len_a = len(a)
    len_b = len(b)
    len_c = len(c)

    # create the matrix
    matrix = [[[0 for i in range(len_c+1)] for j in range(len_b+1)] for k in range(len_a+1)]

    for i in range(len_a + 1):
        for j in range(len_b + 1):
            for k in range(len_c + 1):

                if i == 0 or j == 0 or k == 0:
                    # print('i='+str(i) + ' j='+str(j) + ' k=' + str(k))
                    matrix[i][j][k] = 0

                elif a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1

                else:
                    matrix[i][j][k] = max(max(matrix[i-1][j][k], matrix[i][j-1][k]), matrix[i][j][k-1])

    if solutiontable:
        for row in matrix:
            print(row)

    #d[len_a][len_b] contains the length of LCS of a[0..len_a-1] & b[0..len_b-1]
    return  matrix[len_a][len_b][len_c]



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
            length_string_3 = random.randint(length_string_1 - 1, length_string_1 + 1)
            
            string_1 = "".join(random.choice(string.ascii_letters) for x in range(length_string_1)).lower()
            string_2 = "".join(random.choice(string.ascii_letters) for x in range(length_string_2)).lower()
            string_3 = "".join(random.choice(string.ascii_letters) for x in range(length_string_3)).lower()

            print(len(string_1))
            print(string_1)
            print(len(string_2))
            print(string_2)
            print(len(string_3))
            print(string_3)

            current_time1 = datetime.datetime.now()
            lcs = lcs3(string_1, string_2, string_3, solutiontable=True)
            current_time2 = datetime.datetime.now()
            
            print('result: ' + str(lcs))
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        an = data[0]
        data = data[1:]
        a = data[:an]
        data = data[an:]
        bn = data[0]
        data = data[1:]
        b = data[:bn]
        data = data[bn:]
        cn = data[0]
        data = data[1:]
        c = data[:cn]
#        print(lcs3(a, b, c))

        if args.solutiontable:
            print(lcs3(a, b, csolutiontable=True))
        else:
            print(lcs3(a, b, c))
