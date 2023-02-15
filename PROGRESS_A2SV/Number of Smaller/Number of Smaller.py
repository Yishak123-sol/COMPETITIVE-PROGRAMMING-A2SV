n, m = list(map(int, input().split(None, 2)))
first_list = list(map(int, input().split(None, n)))
second_list = list(map(int, input().split(None, m)))
count = i = j = 0
ans = []
 
while i < n and j < m:
    if second_list[j] > first_list[i]:
        i += 1
        count += 1
    else:
        ans.append(count)
        j += 1
 
while j < m:
    ans.append(count)
    j += 1
    
print(*ans)
