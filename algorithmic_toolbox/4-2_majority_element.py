# Uses python3

import argparse
import datetime
import random
import sys


# def get_majority_element_fast(nrcall, a, left, right):
    
#     # if array is only 2 elements long, the base case is reached
#     # and a majority element is determined
#     if left == right:
#         print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#         print('return '  + str(nrcall) + ': ' + str(a[left]))
#         print('-----')
#         return a[left]

#     if left + 1 == right:
#         if a[left] == a[right]:
#             print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#             print('return A2 ' + str(nrcall) + ': '  + str(a[left]))
#             print('-----')
#             return a[left]
#         else:
#             print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#             print('return '  + str(nrcall) + ': -1')
#             print('-----')
#             return -1

#     # in every other case
#     # split array in half and determine majority on each halves
#     mid = int(left + (right - left) / 2)

#     length_left_halve = mid - left + 1
#     length_right_halve = right - (mid + 1) + 1

#     majority_left_halve = get_majority_element_fast(nrcall+1, a, left, mid)
#     majority_right_halve = get_majority_element_fast(nrcall+1, a, mid+1, right)

#     print('left_length is ' + str(length_left_halve))
#     print('right_length is ' + str(length_right_halve))
#     if length_left_halve > length_right_halve:
#         print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#         print('return X: ' + str(nrcall) + ': '  + str(majority_left_halve))
#         print('-----')
#         return majority_left_halve
#     elif length_right_halve > length_left_halve:
#         print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#         print('return Y: ' + str(nrcall) + ': '  + str(majority_right_halve))
#         print('-----')
#         return majority_right_halve

#     if majority_left_halve == -1 and majority_right_halve >= 0:
#         return majority_right_halve
#     elif majority_right_halve == -1 and majority_left_halve >= 0:
#         return majority_left_halve


#     if majority_left_halve == majority_right_halve:
#         print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#         print('return B: ' + str(nrcall) + ': '  + str(majority_left_halve))
#         print('-----')
#         return majority_left_halve
#     else:
#         print('call ' + str(nrcall) + ': ' + str(left) + ' ' + str(right) )
#         print('return C: ' + str(nrcall) + ': -1')
#         print('-----')
#         return -1




def get_majority_element_naive(a, left, right):
    
    count = {}

    for i in range(0, len(a)):

        if a[i] in count:
            count[a[i]] += 1
        else:
            count[a[i]] = 1

    #print(count)
    #print(max(count.values()))
    #print(int(len(a)/2))

    if (max(count.values()) > int(len(a)/2)):
        return 1
    else:
        return -1

if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-18'

    parser = argparse.ArgumentParser(description='majority element',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    # parser.add_argument('--stresstest', action='store_true',
    #                    help='perform a stress test')
    # parser.add_argument('--fast', action='store_true',
    #                    help='use the fast algorithm')
    # parser.add_argument('--naive', action='store_true',
    #                    help='use the naive algorithm')

    args = parser.parse_args()
   
    # # perform stress test?
    # if args.stresstest:

    #     while(True):

    #         n = random.randint(1, 5)
    #         print(n)

    #         a = []

    #         createSequenceWithMajority = bool(random.getrandbits(1))

    #         if(createSequenceWithMajority):
    #             print('creating a list with a majority element')
    #             # how often should the majority element be put in list
    #             amountMajorityElement = random.randint(int(n/2+1), n)

    #             # how often the other elements
    #             amountOtherElements = n - amountMajorityElement

    #             # what should the majority element be
    #             majorityElement = random.randint(0, 100)

    #             # put the majority element in list
    #             a = [majorityElement] * amountMajorityElement

    #             # fill list with other random elements
    #             for i in range(0, amountOtherElements):
    #                 a.append(random.randint(0, 100))

    #         else:
    #             print('creating a list withOUT a majority element')
    #             # fill list with other random elements
    #             for i in range(0, n):
    #                 a.append(random.randint(0, 100))

    #         # shuffle list
    #         random.shuffle(a)
            
    #         # print list
    #         print(' '.join(str(lulu) for lulu in a ))

    #         # run the algos
    #         current_time1 = datetime.datetime.now()
    #         res1 = get_majority_element_naive(a, 0, len(a)-1)
    #         res_naive = 0
    #         if res1 != -1:
    #             res_naive = 1

    #         current_time2 = datetime.datetime.now()
    #         res2 = get_majority_element_fast(1, a, 0, len(a)-1)
    #         res_fast = 0
    #         if res2 != -1:
    #             res_fast = 1

    #         current_time3 = datetime.datetime.now()

    #         if res_naive != res_fast:
    #             print("ERROR: result naive: " + str(res_naive))
    #             print("ERROR: result fast: " + str(res_fast))
    #             break
    #         else:
    #             print('OK: ' + str(res_naive))
    #             print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

    #         print('------')

    # elif args.fast:
    #     input = sys.stdin.read()
    #     n, *a = list(map(int, input.split()))
    #     majority_element = get_majority_element_fast(1, a, 0, n-1)
    #     if majority_element != -1:
    #         #print('1 majority element is ' + str(majority_element))
    #         print(1)
    #     else:
    #         print(0)

    # elif args.naive:
    #     input = sys.stdin.read()
    #     n, *a = list(map(int, input.split()))
    #     if get_majority_element_naive(a, 0, n-1) != -1:
    #         print(1)
    #     else:
    #         print(0)

    # # this is called when no arguments are used
    # else:
    #     input = sys.stdin.read()
    #     n, *a = list(map(int, input.split()))
    #     if get_majority_element_fast(1, a, 0, n-1) != -1:
    #         print(1)
    #     else:
    #         print(0)

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_naive(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)



# original programming assignment

'''
### 4.2 Majority Element

#### Problem Introduction
Majority rule is a decision rule that selects the alternative which has a majority, that is, more than half the votes. Given a sequence of elements a_1 , a_2 , . . . , a_n , you would like to check whether it contains an element that appears more than n/2 times. A naive way to do this is the following.

```
MajorityElement(a_1 , a_2 , . . . , a_n ):
for i from 1 to n:
currentElement ← a_i
count ← 0
for j from 1 to n:
if a j = currentElement:
count ← count + 1
if count > n/2:
return a_i
return “no majority element”
```

The running time of this algorithm is quadratic. Your goal is to use the divide-and-conquer technique to
design an O(n log n) algorithm.

#### Problem Description
**Task:** The goal in this code problem is to check whether an input sequence contains a majority element.
**Input Format:** The first line contains an integer n, the next one contains a sequence of n non-negative
integers a_0, a_1, . . . , a_n−1 .
**Constraints:** 1 ≤ n ≤ 10^5 ; 0 ≤ a_i ≤ 10^9 for all 0 ≤ i < n.
**Output Format:** Output 1 if the sequence contains an element that appears strictly more than n/2 times,
and 0 otherwise.

#### Sample 1

*Input:*
5
2 3 9 2 2

*Output:*
1
2 is the majority element.

#### Sample 2

*Input:*
4
1 2 3 4

*Output:*
0
There is no majority element in this sequence.

#### Sample 3

*Input:*
4
1 2 31

*Output:*
0
This sequence also does not have a majority element (note that the element 1 appears twice and hence
is not a majority element).

#### What To Do
This problem can be solved by the divide-and-conquer algorithm in time O(n log n). Indeed, if a sequence of length n contains a majority element, then the same element is also a majority element for one of its halves. Thus, to solve this problem you first split a given sequence into halves and make two recursive calls. Do you see how to combine the results of two recursive calls?
It is interesting to note that this problem can also be solved in O(n) time by a more advanced (non-divide-and-conquer) algorithm that just scans the given sequence twice.

#### Implementation in Python

'''
