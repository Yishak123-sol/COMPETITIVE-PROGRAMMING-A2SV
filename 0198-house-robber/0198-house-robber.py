class Solution:
    def rob(self, nums: List[int]) -> int:
        print(len(nums))
        self.memo = {}
        if len(nums) == 1:return nums[0]
        if len(nums) == 2:return max(nums[0], nums[1])
        
        return self.helper(len(nums)-1, nums)
    
    def helper(self, idx, nums):
        if idx < 0:return 0
        if idx == 0:return nums[0]
        if idx == 1:return max(nums[0], nums[1])
        
        if idx-2 not in self.memo:
            self.memo[idx-2] = self.helper(idx-2, nums)
        if idx -1 not in self.memo:
            self.memo[idx-1] = self.helper(idx-1, nums)
            
        return max(self.memo[idx-2]+nums[idx], self.memo[idx-1])
    
    
    
    
    
    
    
    
    

    
    
    