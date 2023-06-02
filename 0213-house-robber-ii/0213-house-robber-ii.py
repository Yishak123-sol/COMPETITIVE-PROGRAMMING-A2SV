class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:return nums[0]
        if len(nums) == 2:return max(nums[0], nums[1])
        if len(nums) == 3:return max(nums[0], nums[1], nums[2])
        
        f = nums[0]
        prev = max(nums[0], nums[1])
        
        for i in range(2, len(nums)-1):
            choice =  max(f+nums[i], prev)
            prev, f = choice, prev
            
        currMaxRobbery = prev
        
        f = nums[1]
        prev = max(nums[1], nums[2])
        for j in range(3, len(nums)):
            choice = max(f+nums[j], prev)
            prev, f = choice, prev
            
        return max(currMaxRobbery, prev)
        
        
        