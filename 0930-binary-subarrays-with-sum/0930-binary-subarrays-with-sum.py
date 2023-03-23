class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        dic = {0:1}
        total = count = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - goal in dic:
                count += dic[total - goal]
            if total in dic:
                dic[total] += 1
            else:
                dic[total] = 1
        
        return count

