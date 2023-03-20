class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]*len(temperatures)
        mon_stack = []
        
        for i in range(len(temperatures)):
            while mon_stack and temperatures[mon_stack[-1]] < temperatures[i]:
                curr = mon_stack.pop()
                ans[curr] = (i-curr)
                
            mon_stack.append(i)
            
        return ans