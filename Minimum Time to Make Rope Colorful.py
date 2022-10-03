class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        left = 0
        sum_ = 0
        prevTime = 0
        
        for right in range(len(colors)):
            if colors[left] == colors[right]:
                min_val = min(prevTime, neededTime[right])
                sum_ += min_val
                prevTime = max(prevTime, neededTime[right])
                
            else:
                prevTime = neededTime[right]
            left = right
            
        return sum_
