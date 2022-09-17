class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count_sum = 0
        start = 0
        end = len(nums) - 1
        
        while start < end:
            total = nums[start] + nums[end]
            if total > k:
                end -= 1
            elif total < k :
                start += 1
            else:
                end -= 1
                start += 1
                count_sum += 1

        return count_sum
