#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num_a = 0
    num_repeats = n // len(s)
    reminder = n % len(s)
    for i in range(len(s)):
        if s[i] == 'a':
            num_a = num_a + num_repeats + (0, 1)[i < reminder]

    return num_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
