n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

i = j = 0
merged = []
while i < n and j < m:
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1


merged += list1[i:]
merged += list2[j:]


print(*merged)
