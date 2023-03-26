class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        res = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == res:
                res += 1
                
        return res