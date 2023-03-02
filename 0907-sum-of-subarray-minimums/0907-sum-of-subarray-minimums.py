class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        modulo = 10**9 + 7
        count = min_sum = 0
        
        for i in range(len(arr)+1):
            while stack and (len(arr) == i or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                count = (mid - left_boundary) * (i - mid) 
                min_sum += count * arr[mid]
        
            stack.append(i)
            
        return min_sum %modulo
    
    