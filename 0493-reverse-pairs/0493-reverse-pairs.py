class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = [0]
        self.mergesort(nums, ans)
        
        return ans[0]
    
    
    def mergesort(self, nums, ans):
        
        if len(nums) == 1:return nums
        
        left,right= self.split(nums)
        left_half = self.mergesort(left, ans)
        right_half = self.mergesort(right, ans)
        
        return self.merge(left_half, right_half, ans)
    
    def merge(self, left, right, ans):
        
        i = 0
        for j in range(len(left)):
            while i < len(right) and left[j] > (right[i] * 2):
                i += 1

            ans[0] += i
                                                
        
        l = r = 0
        temp = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                temp.append(left[l])
                l += 1
            else:
                temp.append(right[r])
                r += 1
                
        while l < len(left):
            temp.append(left[l])
            l += 1
        
        while r < len(right):
            temp.append(right[r])
            r += 1
            
        return temp
            
    def split(self, nums):
        
        length = len(nums)
        
        mid = length//2
        left = nums[:mid]
        right = nums[mid:]
        
        return left, right
            
    
    
    
    
    
    
    
    
    
    
    
    
    