class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:return nums[0]
        f  = nums[0]
        s = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            total = nums[i] + f
            choice = max(total, s)
            
            s, f = choice, s
            
        return s