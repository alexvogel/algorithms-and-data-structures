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

