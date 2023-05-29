from collections import defaultdict
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        memo = defaultdict(int)
        nums = [0]*(n+1)
        
        for i in range(n+1):
            nums[i] = self.helper(i, memo, nums)
            
        return max(nums)
    
    
    def helper(self, n, memo, nums):
        
        idx = n//2
        if n == 0:return 0
        if n == 1:return 1
        
        if n % 2 == 0:
            if not memo[idx]:
                memo[idx] = self.helper(idx, memo, nums)
                
            return memo[idx]
        
        if n % 2 != 0:
            if not memo[idx]:
                idx = n//2
                memo[idx] = self.helper(idx, memo, nums)
            if not memo[idx+1]:
                idx = n//2
                memo[idx+1] = self.helper(idx+1, memo, nums)
                
            return memo[idx] + memo[idx+1]