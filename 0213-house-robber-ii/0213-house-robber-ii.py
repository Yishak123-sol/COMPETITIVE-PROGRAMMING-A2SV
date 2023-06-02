class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:return nums[0]
        if len(nums) == 2:return max(nums[0], nums[1])
        if len(nums) == 3:return max(nums[0], nums[1], nums[2])
        
        memo = {}
        robbery_choice1 = self.dp(nums, 0, len(nums)-2, memo)
        memo = {}
        robbery_choice2 = self.dp(nums, 1, len(nums)-1, memo)
        
        
        return max(robbery_choice1, robbery_choice2)
    
    def dp(self, nums,start, idx, memo):
       
        if idx == start:return nums[start]
        if idx == start+1:return max(nums[start], nums[start+1])
        
        if idx - 2 not in memo:
            memo[idx-2] = self.dp(nums, start, idx-2, memo)
            
        if idx - 1 not in memo:
            memo[idx-1] = self.dp(nums, start, idx-1, memo)
            
        return max(memo[idx-1], memo[idx-2] + nums[idx])
        
        
        
        
        
