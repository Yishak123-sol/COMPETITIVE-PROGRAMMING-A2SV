class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        index_total = 0
        for index in range(len(nums)):
            total -= nums[index]
            if total == index_total:
                return index
            
            index_total += nums[index]
            
        return -1
