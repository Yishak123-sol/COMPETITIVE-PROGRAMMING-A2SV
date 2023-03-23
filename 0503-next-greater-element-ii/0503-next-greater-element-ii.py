class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        greater = defaultdict(int)
        stack = []
        length = len(nums)
        
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                smaller = stack.pop() 
                greater[smaller] = nums[i]
            stack.append(i)
        
        
        res = [-1] * length
        for j in range(len(stack)):
            idx = stack[j]
            for i in range(idx):
                if nums[i] > nums[idx] :
                    greater[idx] = nums[i]
                    break
        for key, values in greater.items():
            res[key] = values
            
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                