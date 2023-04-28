class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = [0]
        self.mergesort(nums, ans, diff)
        
        return ans[0]
    
    def mergesort(self, nums, ans, diff):
        
        if len(nums) == 1:return nums
        
        left, right = self.split(nums)
        left_half = self.mergesort(left, ans, diff)
        right_half = self.mergesort(right, ans, diff)
        
        return self.merge(left_half, right_half, ans, diff)
    
    def split(self, nums):
        
        length = len(nums)
        
        mid = length//2
        left = nums[:mid]
        right = nums[mid:]
        
        return left, right
    
    def merge(self, left, right, ans, diff):
        
        i = 0
        for j in range(len(left)):
        
            while i < len(right) and left[j] > (right[i] + diff):
                i += 1
                
            ans[0] += len(right) - i
            
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
            r+= 1
            
        return temp
                
                
        