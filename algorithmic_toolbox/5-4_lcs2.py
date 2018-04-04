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
