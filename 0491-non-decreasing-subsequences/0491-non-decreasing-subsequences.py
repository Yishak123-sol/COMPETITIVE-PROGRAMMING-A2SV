class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.nums = nums
        self.ans = set()
        
        self.helper(0, [])
        
        return self.ans
    def helper(self, idx, temp):
        
        if idx == len(self.nums):
            if len(temp) >= 2:
                self.ans.add(tuple(temp))
            return 
            
        if (not temp) or temp[-1] <= self.nums[idx]:
            temp.append(self.nums[idx])
            self.helper(idx+1, temp)
            temp.pop()
            
        self.helper(idx+1, temp)
        
            
            
            
            
        