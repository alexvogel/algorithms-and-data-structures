# Uses python3
import argparse
import random
import sys
import datetime
from collections import namedtuple

def getGreaterOrEqual(digit, maxDigit):

    a = str(digit) + str(maxDigit)
    b = str(maxDigit) + str(digit)

    if a > b:
        return digit
    else:
        return maxDigit

def largest_number(a):
    #write your code here
    res = ''

    while(len(a) > 0):
        maxDigit = -9999

        for digit in a:

            maxDigit = getGreaterOrEqual(digit, maxDigit)

        res += maxDigit

        #print('remove digit ' + str(maxDigit) + ' from list ' + str(a))
        a.remove(str(maxDigit))


    return res


if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-13'

    parser = argparse.ArgumentParser(description='different summands',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 10)
            print(n)

            numbers = []
            for i in range(1, n):
                numbers.append(str(random.randint(1, 1000)))

            for number in numbers:
                print(number, end=' ')
            print("\n")

            current_time1 = datetime.datetime.now()
            res = largest_number(numbers)
            current_time2 = datetime.datetime.now()

            print(res)
            
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = input.split()
        a = data[1:]
        print(largest_number(a))



# original programming assignment

'''
### 3.6 Maximum Salary

#### Problem Introduction
As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number.

We considered the following algorithm for composing the largest number out of the given *single-digit numbers*.

```
LargestNumber(Digits):
answer ← empty string
while Digits is not empty:
maxDigit ← −∞
for digit in Digits:
if digit ≥ maxDigit:
maxDigit ← digit
append maxDigit to answer
remove maxDigit from Digits
return answer
```

Unfortunately, this algorithm works only in case the input consists of single-digit numbers. For example, for an input consisting of two integers 23 and 3 (23 is not a single-digit number!) it returns 233, while the largest number is in fact 323. In other words, using the largest number from the input as the first number is not a *safe move*.
The goal in this problem is to tweak the above algorithm so that it works not only for single-digit numbers, but for arbitrary positive integers.

#### Problem Description
**Task:** Compose the largest number out of a set of integers.
**Input Format:** The first line of the input contains an integer n. The second line contains integers
a_1 , a_2 , . . . , a_n .
**Constraints:** 1 ≤ n ≤ 100; 1 ≤ a_i ≤ 10^3 for all 1 ≤ i ≤ n.
**Output Format:** Output the largest number that can be composed out of a_1 , a_2 , . . . , a_n .

#### Sample 1

*Input:*
2
21 2

*Output:*
221
Note that in this case the above algorithm also returns an incorrect answer 212.

#### Sample 2

*Input:*
5
9 4 6 1 9

*Output:*
99641
In this case, the input consists of single-digit numbers only, so the algorithm above computes the right
answer.

#### Sample 3

*Input:*
3
23 39 92

*Output:
923923
As a coincidence, for this input the above algorithm produces the right result, though the input does
not have any single-digit numbers.

#### What To Do?
Interestingly, for solving this problem, all one need to do is to replace the check digit ≥ maxDigit with a call IsGreaterOrEqual(digit, maxDigit) for an appropriately implemented function IsGreaterOrEqual.
For example, IsGreaterOrEqual(2, 21) should return True.

#### Implementation in Python

'''
