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
