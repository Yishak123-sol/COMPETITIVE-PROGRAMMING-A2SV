
length = list(map(int, input().split()))
list_1 = list(map(int, input().split()))
left = 0
res = 100000000000000000
total = 0
 
for right in range(len(list_1)):
    total += list_1[right]
    while total >= length[1]:
        res = min(res, right-left+1)
        total -= list_1[left]
        left += 1
    
if res == 100000000000000000:
    print(-1)
else:
    print(res)
 
    
