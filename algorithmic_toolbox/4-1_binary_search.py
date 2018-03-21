# Uses python3

import argparse
import datetime
import random
import sys

def binary_search(a, low, high, x):

#    print('x=' + str(x) + '    low=' + str(low) + '   high=' + str(high))

    if high < low:
#        print('A gefunden: ' + str(-1))
#        print('---')
        return -1

    mid = int(low + ((high - low) / 2))
#    print('mid_ungerundet=' + str(low + (high - low) / 2))
#    print('mid=' + str(mid))

    if x == a[mid]:
#        print('B gefunden: ' + str(mid))
#        print('---')
        return mid
    elif x < a[mid]:
#        print('suche in der unteren haelfte')
        return binary_search(a, low, mid-1, x)
    elif x > a[mid]:
#        print('suche in der oberen haelfte')
        return binary_search(a, mid+1, high, x)



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-17'

    parser = argparse.ArgumentParser(description='binary search',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')
    parser.add_argument('--fast', action='store_true',
                       help='use the fast algorithm')
    parser.add_argument('--naive', action='store_true',
                       help='use the naive algorithm')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 1000)
            k = random.randint(1, 1000)

            print(n, end=' ')
            a = []
            for i in range (0, n):
                rand_a = random.randint(0, 1000000)
                a.append(rand_a)
            
            # remove duplicates
            a = list(set(a))

            # sort
            a = sorted(a)

            # evtl removed duplicates changed the amount of numbers - so correct for that
            n = len(a)

            print(' '.join(str(lulu) for lulu in a ))

            print(k, end=' ')
            b = []
            for i in range (0, k):

                if(bool(random.getrandbits(1))):

                    random_index = random.randint(0, n-1)
                    b.append(a[random_index])
                    print(a[random_index], end=' ')

                else:
                    rand_b = random.randint(0, 1000000)
                    print(rand_b, end=' ')
                    b.append(rand_b)
            
            print("\n")

            current_time1 = datetime.datetime.now()
            res_linear = []
            for i in range(0, k):
                res_linear.append(linear_search(a, b[i]))

            current_time2 = datetime.datetime.now()
            res_binary = []
            for i in range(0, k):
                res_binary.append(binary_search(a, 0, len(a)-1, b[i]))

            current_time3 = datetime.datetime.now()

            if(set(res_linear)^set(res_binary)):
                print("ALARM: result naive: " + ' '.join(str(res_linear)))
                print("ALARM: result binary: " + ' '.join(str(res_binary)))
                break
            else:
                print('OK:' + ' '.join(str(res_linear)))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')

    elif args.fast:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]
        a = data[1 : n + 1]
        for x in data[n + 2:]:
            # replace with the call to binary_search when implemented
            print(binary_search(a, 0, len(a)-1, x), end = ' ')

    elif args.naive:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]
        a = data[1 : n + 1]
        for x in data[n + 2:]:
            # replace with the call to binary_search when implemented
            print(linear_search(a, x), end = ' ')


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]
        a = data[1 : n + 1]
        for x in data[n + 2:]:
            # replace with the call to binary_search when implemented
            print(binary_search(a, 0, len(a)-1, x), end = ' ')
