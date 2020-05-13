#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    moves = 0
    h_low_max = 0
    h_up_max = 0
    v_low_max = 0
    v_up_max = 0
    pos_low_max = 0
    pos_up_max = 0
    neg_low_max = 0
    neg_up_max = 0

    if (n <= 0):
        return 0

    """ Find the sum of total possible moves """
    """ For both vertical and horizontal directions """
    moves += (2*n - 2)
    """ Directions for diagonal slope 1 """
    moves += (n - abs(c_q - r_q) - 1)
    """ Directions for diagonal slope -1 """
    if ((c_q + r_q) < (n + 1)):
        moves += (r_q + c_q - 2)
    elif ((r_q + c_q) > (n + 1)):
        moves += (2*n - r_q - c_q)
    else:
        moves += (n - 1)
    
    #print("Total possible moves: %d" % moves)

    """ Find obstacles """
    for [r_o, c_o] in obstacles:
        if (c_q == c_o):
            """ Obstacle in vertical line """
            if (r_o < r_q):
                v_low_max = max(r_o, v_low_max)
            elif (r_o > r_q):
                v_up_max = max(n - r_o + 1, v_up_max)
            #print("After Obstacles in vertical line %d " % moves)
        elif (r_q == r_o):
            """ Obstacle in horizontal line """
            if (c_o < c_q):
                h_low_max = max(c_o, h_low_max)
            elif (c_o > c_q):
                h_up_max = max(n - c_o + 1, h_up_max)
            #print("After Obstacles in horizontal line %d " % moves)
        elif ((c_o - r_o) == (c_q - r_q)):
            """ Obstacle in positive slope diagonal line """
            if (c_q > r_q):
                if (c_o < c_q):
                    pos_low_max = max(r_o, pos_low_max)
                elif (c_o > c_q):
                    pos_up_max = max(n - c_o + 1, pos_up_max)
            elif (c_q <= r_q):
                if (c_o < c_q):
                    pos_low_max = max(c_o, pos_low_max)
                elif (c_o > c_q):
                    pos_up_max = max(n - r_o + 1, pos_up_max)
            #print("After Obstacles in positive slop %d " % moves)
        elif ((c_o + r_o) == (c_q + r_q)):
            """ Obstacle in negative slope diagonal line """
            if ((c_q + r_q) < (n + 1)):
                if (c_o < c_q):
                    neg_low_max = max(c_o, neg_low_max)
                elif (c_o > c_q):
                    neg_up_max = max(r_o, neg_up_max)
            elif ((c_q + r_q) >= (n + 1)):
                if (c_o < c_q):
                    neg_low_max = max(n - r_o + 1, neg_low_max)
                elif (c_o > c_q):
                    neg_up_max = max(n - c_o + 1, neg_up_max)
            #print("After Obstacles in negative slop %d " % moves)
    moves -= h_low_max
    moves -= h_up_max
    moves -= v_low_max
    moves -= v_up_max
    moves -= pos_low_max
    moves -= pos_up_max
    moves -= neg_low_max
    moves -= neg_up_max
    return moves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
