class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if idx >= 0 and idx < len(nums):
                if nums[idx] == 0:
                    nums[idx] = -(len(nums)+2)
                elif nums[idx] > 0:
                    nums[idx] = -nums[idx]
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
            
        return i+2