class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return False
        
        stack = []
        curr_min = nums[0]
        for num in nums[1:]:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:return True
            curr_min = min(curr_min, num)
            stack.append([num, curr_min])
            
        return False
    
    