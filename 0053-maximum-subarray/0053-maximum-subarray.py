class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_val = nums[0]
        cur_sum = 0

        for R in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                
            cur_sum += nums[R]
            if cur_sum >= max_val:
                max_val = cur_sum
                
        return max_val
    

    
    
    