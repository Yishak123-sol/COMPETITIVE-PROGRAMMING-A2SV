class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.ans = set()
        nums = [i for i in range(1, n+1)]
        print(nums)
        self.helper(0, nums, [])
        
        return self.ans
    
    def helper(self, idx, nums, temp):
        
        if idx == len(nums):
            if len(temp) == self.k:
                self.ans.add(tuple(temp))
            return 
        
        if idx < len(nums):
            temp.append(nums[idx])
            self.helper(idx+1, nums, temp)
            temp.pop()
            
        self.helper(idx+1, nums, temp)
            
        
                
        
        
            
        