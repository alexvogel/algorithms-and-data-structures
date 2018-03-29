# Uses python3

import argparse
import datetime
import random
import collections
import sys
import time
import math
import statistics


# clac the distance
def dist_points(p1, p2):
    return math.sqrt( (p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2 )
    #return ( (p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2 ) ** .5

# calc the distance
def dist(x1, y1, x2, y2):
    return math.sqrt( pow(x2-x1, 2) + pow(y2-y1, 2) )

# this is called first
def minimum_distance_fast(x, y):

    a = list(zip(x, y)) # This produces a list of tuples

    points_sorted_by_x = sorted(a, key=lambda x: x[0]) # sorting by x
    points_sorted_by_y = sorted(a, key=lambda x: x[1]) # sorting by y
    #p1, p2, mi = minimum_distance_fast_recursive_call(points_sorted_by_x, points_sorted_by_y)
    mi = minimum_distance_fast_recursive_call(points_sorted_by_x, points_sorted_by_y)

    return mi

def minimum_distance_fast_strip(points_sorted_by_x, points_sorted_by_y, delta):

    # its faster to assign the length to a variable - we'll use it more than once
    amount_points = len(points_sorted_by_x)

    # to devide the point set by a vertical line, I need to find the point with the median x coordinate
    x_mid = points_sorted_by_x[amount_points // 2][0]

    # create an array of points not further than delta from midpoint on x-sorted array
    points_strip_sorted_by_y = [x for x in points_sorted_by_y if x_mid - delta <= x[0] <= x_mid + delta]

    # start with known minimum so far
    smallest_distance = delta

    amount_points_strip = len(points_strip_sorted_by_y)

    for i in range (amount_points_strip-1):
        for j in range(i+1, min(i + 7, amount_points_strip)):
            p1, p2 = points_strip_sorted_by_y[i], points_strip_sorted_by_y[j]

            # optimization: calc the distance only if y coordinate differs less than current minimum
            if abs(p1[1] - p2[1]) < smallest_distance:

                distance = dist_points(p1, p2)

                if distance < smallest_distance:
                    smallest_distance = distance
                    #best_pair = p1, p2

    #return best_pair[0], best_pair[1], smallest_distance
    return smallest_distance

# this is the recursive call
def minimum_distance_fast_recursive_call(points_sorted_by_x, points_sorted_by_y):

    # print('length of pointlist: ' + str(len(points_sorted_by_x)))

    # its faster to assign the length to a variable - we'll use it more than once
    amount_points = len(points_sorted_by_x)

    # if there are 3 or less points, then use the naive approach
    if amount_points <= 3:
        return minimum_distance_naive2(points_sorted_by_x)

    # to devide the point set by a vertical line, I need to find the point with the median x coordinate
    x_mid_index = amount_points // 2
    x_mid = points_sorted_by_x[x_mid_index][0]

    # points sorted by x left and right of the vertical line that divides the points at the midpoint with x=x_mid
    Lx = points_sorted_by_x[:x_mid_index]
    Rx = points_sorted_by_x[x_mid_index:]

    Ly = sorted(Lx, key=lambda x: x[1]) # sorting by y
    Ry = sorted(Rx, key=lambda x: x[1]) # sorting by y

    # # points sorted by y left and right of the vertical line that divides the points at the midpoint with x=x_mid
    # Lx_set = set(Lx)
    # Ly = list()
    # Ry = list()

    # # split points_sorted_by_y into 2 arrays using midpoint

    # for point in points_sorted_by_y:
    #     if point in Lx_set:
    #         Ly.append(point)
    #     else:
    #         Ry.append(point)

    # call recursively with left and right point list
#    (pl_1, pl_2, mi_left) = minimum_distance_fast_recursive_call(Lx, Ly)
#    (pr_1, pr_2, mi_right) = minimum_distance_fast_recursive_call(Rx, Ry)
    mi_left = minimum_distance_fast_recursive_call(Lx, Ly)
    mi_right = minimum_distance_fast_recursive_call(Rx, Ry)

    # determine smallest distance
#    mi_min = None
#    point_pair = None
    if mi_left <= mi_right:
        mi_min = mi_left
#        point_pair = (pl_1, pl_2)
    else:
        mi_min = mi_right
#        point_pair = (pr_1, pr_2)

    # calc the closest distance in the strip around the dividing vertical line
#    (ps_1, ps_2, mi_strip) = minimum_distance_fast_strip(points_sorted_by_x, points_sorted_by_y, mi_min, point_pair)
    mi_strip = minimum_distance_fast_strip(points_sorted_by_x, points_sorted_by_y, mi_min)

    # smallest distance in whole point list
    if mi_min <= mi_strip:
#        return point_pair[0], point_pair[1], mi_min
        return mi_min
    else:
        return mi_strip


# def minimum_distance_naive2(ax):
#     mi = dist_points(ax[0], ax[1])
#     p1 = ax[0]
#     p2 = ax[1]
#     ln_ax = len(ax)
#     if ln_ax == 2:
#         return p1, p2, mi
#     for i in range(ln_ax-1):
#         for j in range(i + 1, ln_ax):
#             if i != 0 and j != 1:
#                 d = dist_points(ax[i], ax[j])
#                 if d < mi:  # Update min_dist and points
#                     mi = d
#                     p1, p2 = ax[i], ax[j]
# #    return p1, p2, mi
#     return mi

def minimum_distance_naive2(points):

    min_distance = None
#    p1 = None
#    p2 = None

    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if i != j:

                distance = dist_points(points[i], points[j])

                if min_distance == None:
                    min_distance = distance
#                    p1 = points[i]
#                    p2 = points[j]
                elif min_distance > distance:
                    min_distance = distance
#                    p1 = points[i]
#                    p2 = points[j]

#    return p1, p2, min_distance
    return min_distance


def minimum_distance_naive(x, y):

    min_distance = None

    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if i != j:

                distance = dist(x[i], y[i], x[j], y[j])

                if min_distance == None:
                    min_distance = distance
                elif min_distance > distance:
                    min_distance = distance

    return min_distance



if __name__ == '__main__':

    version = '0.1'
    date = '2018-03-26'

    parser = argparse.ArgumentParser(description='closest points',
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

            # amount of points
            n = random.randint(2, 1000)

            min_coord = -10000
            max_coord = 10000

            # print amount of points in first line
            print(n)

            x = []
            y = []

            # generate points
            for i in range(0, n):

                random_x = random.randint(min_coord, max_coord)
                random_y = random.randint(min_coord, max_coord)

                x.append(random_x)
                y.append(random_y)

                print(str(random_x) + ' ' + str(random_y))

            current_time1 = datetime.datetime.now()
            res_naive = minimum_distance_naive(x, y)

            current_time2 = datetime.datetime.now()
            res_fast = minimum_distance_fast(x, y)

            current_time3 = datetime.datetime.now()

            if(res_naive != res_fast):
                print("ALARM: result naive: " + str(res_naive))
                print("ALARM: result fast: " + str(res_fast))
                break
            else:
                print('OK:' + str(res_naive))
                print('time consumed: naive:' + str(current_time2-current_time1) + ' fast:' + str(current_time3-current_time2))

            print('------')


    elif args.fast:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        print("{0:.9f}".format(minimum_distance_fast(x, y)))

    elif args.naive:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        print("{0:.9f}".format(minimum_distance_naive(x, y)))

    # this is called when no arguments are used
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        x = data[1::2]
        y = data[2::2]
        print("{0:.9f}".format(minimum_distance_fast(x, y)))
