class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        left_half, right_half = self.split(nums)
        left = self.sortArray(left_half)
        right = self.sortArray(right_half)
        
        return self.merge(left, right)
    
    def split(self, list):
        
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        
        return left, right
    
    def merge(self, left, right):
        
        res = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                
        while i < len(left):
            res.append(left[i])
            i += 1
            
        while j < len(right):
            res.append(right[j])
            j += 1
            
        return res