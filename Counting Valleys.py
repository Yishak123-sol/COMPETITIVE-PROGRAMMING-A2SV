import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valley_count= 0
    sea_level = 0
    hill = []
    for i in path:
        if i=="d":
            sea_level -= 1
            hill.append(sea_level)
        else:
            sea_level += 1
            hill.append(sea_level)

    for j in range(len(hill)):
        if hill[j] == -1 and hill[j+1] == 0:
            valley_count += 1
    
    return valley_count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input().lower()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
