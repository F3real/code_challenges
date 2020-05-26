#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    min_distance = 10**5 + 1 # greater then max constraint
    indexes = {}
    for i in range(len(a)):
        if a[i] in indexes:
            distance = i - indexes[a[i]]
            if distance < min_distance:
                min_distance = distance
        indexes[a[i]] = i
    if (10**5 + 1) == min_distance:
        min_distance = -1
    return min_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = map(int, raw_input().rstrip().split())

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()