class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        for i in range(1, length+1):
            res = (res^nums[i-1]^i)
            
        return res