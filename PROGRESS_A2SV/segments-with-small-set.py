length, target = list(map(int, input().split()))
arr =  list(map(int, input().split()))

res = 0
left = 0
temp = {}

for right in range(length):

    if arr[right] in temp:
        temp[arr[right]] += 1
    else:
        temp[arr[right]] = 1

    while len(temp) > target:
        temp[arr[left]] -= 1
        if temp[arr[left]] == 0:
            del temp[arr[left]]

        left += 1

    res += (right - left + 1)

print(res)
