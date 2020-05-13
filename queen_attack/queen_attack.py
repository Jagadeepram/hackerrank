#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    moves = 0
    h_low_list = [0]
    h_up_list = [0]
    v_low_list = [0]
    v_up_list = [0]
    pos_low_list = [0]
    pos_up_list = [0]
    neg_low_list = [0]
    neg_up_list = [0]

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
                v_low_list.append(r_o)
            elif (r_o > r_q):
                v_up_list.append(n - r_o + 1)
            #print("After Obstacles in vertical line %d " % moves)
        elif (r_q == r_o):
            """ Obstacle in horizontal line """
            if (c_o < c_q):
                h_low_list.append(c_o)
            elif (c_o > c_q):
                h_up_list.append(n - c_o + 1)
            #print("After Obstacles in horizontal line %d " % moves)
        elif ((c_o - r_o) == (c_q - r_q)):
            """ Obstacle in positive diagonal line """
            if (c_q > r_q):
                if (c_o < c_q):
                    pos_low_list.append(r_o)
                elif (c_o > c_q):
                    pos_up_list.append(n - c_o + 1)
            elif (c_q <= r_q):
                if (c_o < c_q):
                    pos_low_list.append(c_o)
                elif (c_o > c_q):
                    pos_up_list.append(n - r_o + 1)
            #print("After Obstacles in positive slop %d " % moves)
        elif ((c_o + r_o) == (c_q + r_q)):
            """ Obstacle in negative diagonal line """
            if ((c_q + r_q) < (n + 1)):
                if (c_o < c_q):
                    neg_low_list.append(c_o)
                elif (c_o > c_q):
                    neg_up_list.append(r_o)
            elif ((c_q + r_q) >= (n + 1)):
                if (c_o < c_q):
                    neg_low_list.append(n - r_o + 1)
                elif (c_o > c_q):
                    neg_up_list.append(n - c_o + 1)
            #print("After Obstacles in negative slop %d " % moves)
    moves -= max(h_low_list)
    moves -= max(h_up_list)
    moves -= max(v_low_list)
    moves -= max(v_up_list)
    moves -= max(pos_low_list)
    moves -= max(pos_up_list)
    moves -= max(neg_low_list)
    moves -= max(neg_up_list)
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
