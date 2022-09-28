class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        
        right_pointer = len(height)-1
        left_pointer, max_water = 0, 0
        
        while right_pointer != left_pointer:
            
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            max_water = max(max_water, area)
            
            if height[right_pointer] > height[left_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
                
        return max_water
