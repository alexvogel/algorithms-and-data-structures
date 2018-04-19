# Uses python3

import argparse
import datetime
import random
import collections
import sys
import time

def count_segments_fast(starts, ends, points):
    cnt = [0] * len(points)

    left_label = 'l'
    point_label = 'p'
    right_label = 'r'

    # use special collection
    point_index = collections.defaultdict(set)

    pairs_coord_label = []
    for start in starts:
        pairs_coord_label.append((start, left_label))

    for end in ends:
        pairs_coord_label.append((end, right_label))

    for i in range(len(points)):
        point = points[i]

        pairs_coord_label.append((point, point_label))
        point_index[point].add(i)

    sorted_pairs_coord_label = sorted(pairs_coord_label, key=lambda x: (x[0], x[1]))

    overlap = 0

    for pair in sorted_pairs_coord_label:

        if pair[1] == left_label:
            overlap += 1

        if pair[1] == right_label:
            overlap -= 1

        if pair[1] == point_label:

            indices = point_index[pair[0]]

            for index in indices:
                cnt[index] = overlap

    return cnt




def count_segments_naive(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-22'

    parser = argparse.ArgumentParser(description='points and segments',
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

            # amount of segments
            s = random.randint(1, 10000)

            # amount of points
            p = random.randint(1, 10000)

            min_coord = -100000
            max_coord = 100000

            print(str(s) + ' ' + str(p))

            # generate sequences
            sequences = []
            sequences_starts = []
            sequences_ends = []

            sequence_length_min = 0
            sequence_length_max = 200

            for i in range(0, s):

                sequence_length = random.randint(sequence_length_min, sequence_length_max)

                sequence_start = random.randint(min_coord, max_coord-sequence_length)

                sequence_end = sequence_start + sequence_length
                
                sequences.append([sequence_start, sequence_end])
                sequences_starts.append(sequence_start)
                sequences_ends.append(sequence_end)

                print(str(sequence_start) + ' ' + str(sequence_end), end=' ')

            print()

            # generate points
            points = []

            for i in range(0, p):
                coord = random.randint(min_coord, max_coord)

                points.append(coord)

                print(str(coord), end=' ')

            print()

            current_time1 = datetime.datetime.now()
            res_naive = count_segments_naive(sequences_starts, sequences_ends, points)

            current_time2 = datetime.datetime.now()
            res_fast = count_segments_fast(sequences_starts, sequences_ends, points)

            current_time3 = datetime.datetime.now()

            if(set(res_naive)^set(res_fast)):
                print("ALARM: result naive: " + ' '.join(str(res_naive)))
                print("ALARM: result fast: " + ' '.join(str(res_fast)))
                break
            else:
                print('OK:' + ' '.join(str(res_naive)))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')

            time.sleep(3)

    elif args.fast:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[1]
        starts = data[2:2 * n + 2:2]
        ends   = data[3:2 * n + 2:2]
        points = data[2 * n + 2:]
        #use fast_count_segments
        cnt = count_segments_fast(starts, ends, points)
        for x in cnt:
            print(x, end=' ')

    elif args.naive:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[1]
        starts = data[2:2 * n + 2:2]
        ends   = data[3:2 * n + 2:2]
        points = data[2 * n + 2:]
        #use fast_count_segments
        cnt = count_segments_naive(starts, ends, points)
        for x in cnt:
            print(x, end=' ')


    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[1]
        starts = data[2:2 * n + 2:2]
        ends   = data[3:2 * n + 2:2]
        points = data[2 * n + 2:]
        #use fast_count_segments
        cnt = count_segments_fast(starts, ends, points)
        for x in cnt:
            print(x, end=' ')



# original programming assignment

'''
### 4.5 Organizing a Lottery

#### Problem Introduction
You are organizing an online lottery. To participate, a person bets on a single
integer. You then draw several ranges of consecutive integers at random.
A participant’s payoff then is proportional to the number of ranges that
contain the participant’s number minus the number of ranges that does not
contain it. You need an efficient algorithm for computing the payoffs for all
participants. A naive way to do this is to simply scan, for all participants, the
list of all ranges. However, you lottery is very popular: you have thousands
of participants and thousands of ranges. For this reason, you cannot afford
a slow naive algorithm.

#### Problem Description
**Task:** You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.
**Input Format:** The first line contains two non-negative integers s and p defining the number of segments
and the number of points on a line, respectively. The next s lines contain two integers a i , b i defining
the i-th segment [a i , b i ]. The next line contains p integers defining points x 1 , x 2 , . . . , x p .
**Constraints:** 1 ≤ s, p ≤ 50000; −10^8 ≤ a_i ≤ b_i ≤ 10^8 for all 0 ≤ i < s; −10^8 ≤ x_j ≤ 10^8 for all 0 ≤ j < p.
**Output Format:** Output p non-negative integers k_0 , k_1 , . . . , k_p−1 where k i is the number of segments which
contain x_i .
More formally, k_i = |{j : a_j ≤ x_i ≤ b_j }| .

#### Sample 1

*Input:*
2 3
0 5
7 10
1 6 11

*Output:*
1 0 0
Here, we have two segments and three points. The first point lies only in the first segment while the
remaining two points are outside of all the given segments.

#### Sample 2

*Input:*
1 3
-10 10
-100 100 0

*Output:*
0 0 1

#### Sample 3

*Input:*
3 2
0 5
-3 2
7 10
1 6

*Output:*
2 0

#### Implementation in Python

'''
