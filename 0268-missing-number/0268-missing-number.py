class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            idx = abs(nums[i])

            if idx < len(nums) and idx != nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return i+1