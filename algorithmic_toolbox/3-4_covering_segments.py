# Uses python3
import argparse
import random
import sys
import datetime
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

# from https://medium.com/competitive/covering-segments-by-points-fc2c56c4b038
def optimal_points(segments):

    # sort the segments by their end points
    segments_endpoint_sorted = sorted(segments, key=lambda x: x.end, reverse=False)
    #print('sorted: ' + str(segments_endpoint_sorted))

    # set the point to the first end point
    point = segments_endpoint_sorted[0].end

    # the list of points
    points = []

    #
    points.append(point)

    for i in range(1, len(segments_endpoint_sorted)):
        if (point < segments_endpoint_sorted[i].start or point > segments_endpoint_sorted[i].end ):
            point = segments_endpoint_sorted[i].end
            points.append(point)

    return points


# def optimal_points(segments):
#     points = []
#     points_seg = {}
#     a = min(segments).start
#     b = max(segments).end

#     for i in range(a, b + 1):
#         seg_id = 0
#         for s in segments:
#             if i >= s.start and i <= s.end:
#                 if i in points_seg:
#                     points_seg[i].append(seg_id)
#                 else:
#                     points_seg[i] = [seg_id]
#             seg_id += 1

#     sort_points_seg = list(sorted(points_seg.items(), key=lambda k: len(k[1]), reverse=True))

#     seg_count = list(range(0, len(segments)))

#     for pto_seg in sort_points_seg:
#         for seg in pto_seg[1]:
#             if len(seg_count) > 0:
#                 if seg in seg_count:
#                     seg_count.remove(seg)
#                     if pto_seg[0] not in points:
#                         points.append(pto_seg[0])

#             else:
#                 return points


#     return points

if __name__ == "__main__":

    version = '0.1'
    date = '2018-03-13'

    parser = argparse.ArgumentParser(description='covering segments',
                                     epilog='author: alexander.vogel@prozesskraft.de | version: ' + version + ' | date: ' + date)
    parser.add_argument('--stresstest', action='store_true',
                       help='perform a stress test')

    args = parser.parse_args()
   
    # perform stress test?
    if args.stresstest:

        while(True):

            n = random.randint(1, 3)
            print(n)

            segments = []

            for i in range(0, n):

                a = random.randint(0, 1000)
                b = random.randint(a, 1000)
                print(str(a) + ' ' + str(b))

                segments.append(Segment(a, b))

            current_time1 = datetime.datetime.now()
            points = optimal_points(segments)
            current_time2 = datetime.datetime.now()

            print(len(points))
            for p in points:
                print(p, end=' ')
            
            print('runtime: ' + str(current_time2-current_time1))
            print('------')

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        n, *data = map(int, input.split())
        segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
        points = optimal_points(segments)
        print(len(points))
        for p in points:
            print(p, end=' ')



# original programming assignment

'''
### 3.4 Collecting Signatures

#### Problem Introduction
You are responsible for collecting signatures from all tenants of a certain building. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as
possible.
The mathematical model for this problem is the following. You are given a set of segments on a line and your goal is to mark as few points on a line as possible so that each segment contains at least one marked point.

#### Problem Description
**Task:** Given a set of n segments {[a_0 , b_0 ], [a_1 , b_1 ], . . . , [a_n−1 , b_n−1 ]} with integer coordinates on a line, find the minimum number m of points such that each segment contains at least one point. That is, find a
set of integers X of the minimum size such that for any segment [a_i , b_i] there is a point x ∈ X such that a_i ≤ x ≤ b_i .
**Input Format:** The first line of the input contains the number n of segments. Each of the following n lines
contains two integers a_i and b_i (separated by a space) defining the coordinates of endpoints of the i-th
segment.
**Constraints:** 1 ≤ n ≤ 100; 0 ≤ a_i ≤ b_i ≤ 10^9 for all 0 ≤ i < n.
**Output Format:** Output the minimum number m of points on the first line and the integer coordinates of m points (separated by spaces) on the second line. You can output the points in any order. If there are many such sets of points, you can output any set. (It is not difficult to see that there always exist a set of points of the minimum size such that all the coordinates of the points are integers.)

#### Sample 1

*Input:*
3
1 3
2 5
3 6

*Output:*
1
3
In this sample, we have three segments: [1, 3], [2, 5], [3, 6] (of length 2, 3, 3 respectively). All of them contain the point with coordinate 3: 1 ≤ 3 ≤ 3, 2 ≤ 3 ≤ 5, 3 ≤ 3 ≤ 6.

#### Sample 2

*Input:*
4
4 7
1 3
2 5
5 6

*Output:*
2
3 6
The second and the third segments contain the point with coordinate 3 while the first and the fourth segments contain the point with coordinate 6. All the four segments cannot be covered by a single point, since the segments [1, 3] and [5, 6] are disjoint.

#### Implementation in Python

'''
