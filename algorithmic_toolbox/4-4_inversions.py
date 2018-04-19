# Uses python3
import sys

def merge(b, c):
    '''
        merges 2 lists in non descending order
        Returns: sorted list, number of inversions

    '''
    merged = []

    inversions = 0

    while b and c:

        if b[0] <= c[0]:
            merged.append(b.pop(0))

        else:
            merged.append(c.pop(0))
            inversions += len(b)

    merged += b or c

    return merged, inversions



def merge_sort(a):
    '''
        algorithm mergesort
        for sorting a list and calculating the needed inversions

        Returns: sorted list, number of inversions
    '''

    length = len(a)

    if length == 1:
        return a, 0

    # calc the floor of middle index
    mid = length // 2

    left_halve, left_halve_inversions = merge_sort(a[0:mid])
    right_halve, right_halve_inversions = merge_sort(a[mid:])

    merged, merged_inversions = merge(left_halve, right_halve)

    all_inversions = merged_inversions + left_halve_inversions + right_halve_inversions

    return merged, all_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    # output only the inversions for this assignment
    print(merge_sort(a)[1])




# original programming assignment

'''
### 4.4 Number of Inversions

#### Problem Introduction
An inversion of a sequence a_0 , a_1 , . . . , a_n−1 is a pair of indices 0 ≤ i < j < n such
that a_i > a_j . The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending
order) sequence contains no inversions at all, while in a sequence sorted in de-
scending order any two elements constitute an inversion (for a total of n(n − 1)/2
inversions).

#### Problem Description
**Task:** The goal in this problem is to count the number of inversions of a given sequence.
**Input Format:** The first line contains an integer n, the next one contains a sequence of integers
a_0 , a_1 , . . . , a_n−1 .
**Constraints:** 1 ≤ n ≤ 10^5 , 1 ≤ a_i ≤ 10^9 for all 0 ≤ i < n.
**Output Format:** Output the number of inversions in the sequence.

#### Sample 1

*Input:*
5
2 3 9 2 9

*Output:*
2
The two inversions here are (1, 3) (a_1 = 3 > 2 = a_3 ) and (2, 3) (a_2 = 9 > 2 = a_3 ).

#### What To Do
This problem can be solved by modifying the merge sort algorithm. For this, we change both the Merge and
MergeSort procedures as follows:
- Merge(B, C) returns the resulting sorted array and the number of pairs (b, c) such that b ∈ B, c ∈ C,
and b > c;
- MergeSort(A) returns a sorted array A and the number of inversions in A.

#### Implementation in Python

'''
