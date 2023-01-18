#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):

    for i in range(0, n - 1):
    
        i += 1
        if arr[n - i] < arr[n - (i+1)]:
            temp = arr[n - i]
            arr[n - i] = arr[n - (i+1)]
            
            for j in arr:
                print(f"{j}", end=" ")
            print("")
            
            arr[n - (i+1)] = temp
            
    for sorted_item in arr:
        print(sorted_item, end=" ")

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
