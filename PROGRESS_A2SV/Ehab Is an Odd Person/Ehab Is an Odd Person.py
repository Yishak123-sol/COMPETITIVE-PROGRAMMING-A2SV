length = int(input())
nums = list(map(int, input().split()))
count_even = 0
count_odd = 0
 
for i in range(len(nums)):
    if nums[i]%2 == 0:
        count_even += 1
    
    else:
        count_odd += 1
 
    if count_even > 0 and count_odd > 0:
        nums.sort()
        print(*nums)
        break
else:
    print(*nums)
