#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    res = "Yes"
    s_len = len(s)
    t_len = len(t)
    max_len = max(s_len, t_len)
    end_of_compare = 0

    if ((s_len + t_len) <= k):
        return res

    for i in range (max_len):
        if (i < s_len and i < t_len):
            if (s[i] != t[i]):
                end_of_compare = 1
        else:
            end_of_compare = 1
        
        if (end_of_compare == 1):
            unmatch_len = s_len - i
            unmatch_len += t_len - i
            if (unmatch_len > k):
                res = "No"
            else:
                if ((k - unmatch_len)%2 == 0):
                    res = "Yes"
                else:
                    res = "No"
            break
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
