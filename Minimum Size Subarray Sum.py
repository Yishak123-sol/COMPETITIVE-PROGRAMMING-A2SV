class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sum_ = 0
        left = 0
        min_diff = len(nums)+1
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= target:
                min_diff = min(min_diff, right-left+1)
                sum_ -= nums[left]
                left += 1
            
        
        return 0 if min_diff == len(nums)+1 else min_diff
        
