
length = list(map(int, input().split()))
list_1 = list(map(int, input().split()))
left = 0
res = 0
total = 0

for right in range(len(list_1)):
    total += list_1[right]
    while total > length[1]:
        total -= list_1[left]
        left += 1
    
    res = max(res, right-left+1)

print(res)
    
