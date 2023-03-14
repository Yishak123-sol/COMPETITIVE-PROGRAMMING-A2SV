class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        left, right, total_odd, count = 0, 0, 0, 0
        
        while right < len(nums):
            if nums[right] % 2 == 1:
                total_odd += 1
                
            if total_odd < k:
                right += 1
                
            elif total_odd == k:
                left_odd, right_odd = 0, 0
                while nums[left] % 2 == 0:
                    left += 1
                    left_odd += 1
                    
                while right < len(nums) - 1 and nums[right + 1] % 2 == 0:
                    right += 1
                    right_odd += 1
                    
                count += (left_odd + 1) * (right_odd + 1)
                left += 1
                total_odd -= 1
                right += 1
            else:
                left += 1
                total_odd -= 1
                
        return count
