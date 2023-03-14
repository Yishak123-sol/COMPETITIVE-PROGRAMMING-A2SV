class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -float("inf")
        left = 0
        store = 0

        for right in range(len(nums)):
            
            store += nums[right]
            if right-left == k-1:
                res = max(res, store/k)
                store -= nums[left]
                left += 1

        return res
