class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = [-1, -1]
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                ans[0] = mid
                
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                ans[-1] = mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        