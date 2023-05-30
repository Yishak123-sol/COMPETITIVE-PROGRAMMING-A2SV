class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.memo = {}
        return self.dp(0, nums, 0, target)
    
    def dp(self, idx, nums, total, target):
        
        if idx == len(nums):return total == target
            
        
        if (idx, total) in self.memo:
            return self.memo[(idx, total)]
            
            
        self.memo[(idx, total)] = self.dp(idx+1, nums, (total + nums[idx]), target) + self.dp(idx+1, nums, (total - nums[idx]), target)
        return self.memo[(idx, total)]