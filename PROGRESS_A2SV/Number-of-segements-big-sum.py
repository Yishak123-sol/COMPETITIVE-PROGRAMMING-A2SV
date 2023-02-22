length, target = list(map(int, input().split()))
arr =  list(map(int, input().split()))

curr = 0
res = 0
left = 0

for right in range(length):

    curr += arr[right]

    while curr >= target:
        res += (length - right)
        curr -= arr[left]
        left += 1

print(res)



