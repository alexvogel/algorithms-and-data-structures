# Uses python3
import sys

def get_change(m):

    coins = (m // 10) + (m % 10) // 5 + (m % 10) % 5

    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))



# original programming assignment

'''
### 3.1 Money Change (Greedy Algorithm)

#### Problem Introduction
In this problem, you will design and implement an elementary greedy algorithm used by cashiers all over the world millions of times per day.

#### Problem Description
**Task:** The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
**Input Format:** The input consists of a single integer m.
**Constraints:** 1 ≤ m ≤ 10^3 .
**Output Format:** Output the minimum number of coins with denominations 1, 5, 10 that changes m.

#### Sample 1

*Input:*
2

*Output:*
2
2 = 1 + 1.

#### Sample 2

*Input:*
28

*Output:*
6
28 = 10 + 10 + 5 + 1 + 1 + 1.

#### Implementation in Python

'''
