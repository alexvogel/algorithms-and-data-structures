# Uses python3
import argparse
import random
import sys
import datetime
import time


def partition3(a, l, r):
    
    m1 = l
    m2 = r

    i = l+1

    x = a[l]

    while(i <= m2):
        if a[i] < x:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1

        elif a[i] > x:
            a[m2], a[i] = a[i], a[m2]
            m2 -= 1

        else:
            i += 1

    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(partitions, a, l, r):
    if l >= r:
        return

    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    if partitions == 2:
        m = partition2(a, l, r)
        randomized_quick_sort(partitions, a, l, m-1);
        randomized_quick_sort(partitions, a, m+1, r);
    elif partitions == 3:
        m1, m2 = partition3(a, l, r)
        print('m1=' + str(m1) + '   m2=' + str(m2))
        #time.sleep(5)
        randomized_quick_sort(partitions, a, l, m1-1);
        randomized_quick_sort(partitions, a, m2+1, r);

    else:
        print('only 2 or 3 partitions allowed')
        sys.exit(1)

    return a


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-19'

    parser = argparse.ArgumentParser(description='majority element',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test comparing the results of the 2-way partiotioned with the 3-way-partioned algorithm')
    parser.add_argument('--stresstest_qs3', action='store_true',
                       help='perform a stress test only on the 3-way partioned algorithm')
    parser.add_argument('--qs2', action='store_true',
                       help='use the quicksort algorithm with 2 partitions')
    parser.add_argument('--qs3', action='store_true',
                       help='use the quicksort algorithm with 3 partitions')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            # how long should the list be
            n = random.randint(10, 100)
            print(n)

            a = []

            # how often should the majority element be put in list
            amountUniqeElements = random.randint(2, min(int(n/3), 50))

            uniqueElements = []

            print('generating a list with ' + str(amountUniqeElements) + ' unique elements')

            # create elements
            for i in range(0, amountUniqeElements):
                rand_int = random.randint(1, 1000)
                uniqueElements.append(rand_int)
                #print(str(i) + ' ' + str(rand_int))

            secure_random = random.SystemRandom()
            # create list
            for i in range(0, n):
                random_choice = secure_random.choice(uniqueElements)
                a.append(random_choice)
                #print('adding unique element to list: ' + str(random_choice))

            # shuffle list
            random.shuffle(a)
            
            #print(a)

            current_time1 = datetime.datetime.now()
            res1 = randomized_quick_sort(2, list(a), 0, len(a)-1)
            #print(res1)
            current_time2 = datetime.datetime.now()
            
            res2 = randomized_quick_sort(3, list(a), 0, len(a)-1)
            #print(res2)
            current_time3 = datetime.datetime.now()


            if(set(res1)^set(res2)):
                print("ALARM: result quicksort with 2 partitions: " + ' '.join(str(res1)))
                print("ALARM: result quicksort with 3 partitions: " + ' '.join(str(res2)))
                break
            else:
                print('OK:' + str(res1))
                print('time consumed: qs2:' + str(current_time2-current_time1) + ' qs3:' + str(current_time3-current_time2))

            print('------')

    elif args.stresstest_qs3:

        while(True):

            # how long should the list be
            n = random.randint(10, 10)
            print(n)

            a = []

            # how often should the majority element be put in list
            amountUniqeElements = random.randint(1, min(int(n/3), 3))

            uniqueElements = []

            print('generating a list with ' + str(amountUniqeElements) + ' unique elements')

            # create elements
            for i in range(0, amountUniqeElements):
                rand_int = random.randint(1, 100)
                uniqueElements.append(rand_int)
                #print(str(i) + ' ' + str(rand_int))

            secure_random = random.SystemRandom()
            # create list
            for i in range(0, n):
                random_choice = secure_random.choice(uniqueElements)
                a.append(random_choice)
                #print('adding unique element to list: ' + str(random_choice))

            # shuffle list
            random.shuffle(a)
            
            #print(a)

            current_time1 = datetime.datetime.now()
            res2 = randomized_quick_sort(3, list(a), 0, len(a)-1)
            #print(res2)
            current_time3 = datetime.datetime.now()

            print('OK:' + str(res2))
            print('time consumed: qs3:' + str(current_time3-current_time1))

            print('------')

    elif args.qs3:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        randomized_quick_sort(3, a, 0, n - 1)
        for x in a:
            print(x, end=' ')

    elif args.qs2:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        randomized_quick_sort(2, a, 0, n - 1)
        for x in a:
            print(x, end=' ')


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        
        # to check the coursera - algorithmic toolbox grader, I use the build in function in python for sorting
        #a = sorted(list(a))
        
        # instead of my own improved quicksort function
        randomized_quick_sort(2, a, 0, n - 1)
        
        for x in a:
            print(x, end=' ')



# original programming assignment

'''
### 4.3 Improving Quick Sort

#### Problem Introduction
The goal in this problem is to redesign a given implementation of the random-
ized quick sort algorithm so that it works fast even on sequences containing
many equal elements.

#### Problem Description
**Task:** To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < x part, = x part, and > x part.
**Input Format:** The first line of the input contains an integer n. The next line contains a sequence of n
integers a_0 , a_1 , . . . , a_n−1 .
**Constraints:** 1 ≤ n ≤ 10^5 ; 1 ≤ a_i ≤ 10^9 for all 0 ≤ i < n.
**Output Format:** Output this sequence sorted in non-decreasing order.

#### Sample 1

*Input:*
5
2 3 9 2 2

*Output:*
2 2 2 3 9

#### What To Do
Implement a 3-way partition procedure and then replace a call to the 2-way partition procedure by a call to
the 3-way partition procedure.

#### Implementation in Python

'''
