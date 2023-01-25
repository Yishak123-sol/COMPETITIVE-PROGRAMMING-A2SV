length, k =  list(map(int, input().split()))
arr = list(map(int, input().split()))
 
arr.sort()
 
 
if k == 0 and arr[k] > 1:
    print(1)
 
elif (k == length and arr[k-1] > 0) or (k < length and arr[k] > arr[k-1] and arr[k] > 0):
    print(arr[k-1])
 
else:
    print(-1)
