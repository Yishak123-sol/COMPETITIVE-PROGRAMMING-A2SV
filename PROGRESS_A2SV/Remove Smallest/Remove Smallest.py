import sys

input = sys.stdin.readline


test_case = int(input())

for _ in range(test_case):

    length = int(input())
    arr = list(map(int, input().split(None, length)))
    
    arr.sort()
    ans = False

    for i in range(1, length):
        if (arr[i] - arr[i-1]) > 1:
           ans = True
          
    print("NO") if ans else print("YES")
