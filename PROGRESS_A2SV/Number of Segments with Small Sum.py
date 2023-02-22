length, target = list(map(int, input().split()))
arr =  list(map(int, input().split()))
left = 0
curr = 0
res = 0

for right in range(len(arr)):
    curr += arr[right]
    while curr > target:
        curr -= arr[left]
        left += 1

    res += (right - left + 1)

print(res)
