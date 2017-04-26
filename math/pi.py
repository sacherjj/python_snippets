import time
import math


def calc_pi(width):
    # Pi = 4 * Area_Circle / Area_Square
    # Calculating 1/4 of the square and circle
    area_square = width * width
    radius_sq = width * width
    area_pi = 0
    for x in range(1, width+1):
        y_val = math.sqrt(radius_sq - x*x)
        area_pi += y_val
    return 4 * area_pi / area_square


def print_calc(width):
    tic = time.clock()
    pi = calc_pi(width)
    toc = time.clock()
    error = math.pi - pi
    print('Width: {}  Time: {}s  Pi: {} with error: {}'.format(width, round(toc - tic, 2), pi, error))


print_calc(10000000000)
# Width: 100000000  Time: 35.8s  Pi: 3.1415926335885564 with error: 2.0001236666900013e-08
# Width: 1000000000  Time: 369.04s  Pi: 3.1415926515893933 with error: 2.000399845769607e-09

