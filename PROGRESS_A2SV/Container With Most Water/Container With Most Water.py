class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0 , len(height)-1
        maxval = 0
        
        while left < right:

            area = height[left] + height[right]
            if height[left] > height[right]:
                area = height[right] * (right-left)
                right -= 1
                
            elif height[left] <= height[right]:
                area = height[left] * (right-left)
                left += 1
            
            maxval = max(maxval, area)
            
            
        return maxval
