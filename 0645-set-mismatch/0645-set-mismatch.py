class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        idx, length = 0, len(nums)
        
        while idx < length:
            value = nums[idx] - 1
            if nums[idx]-1 != idx and nums[value] != nums[idx]:
                nums[idx], nums[value] = nums[value], nums[idx]
            else:
                idx += 1
                
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
                res.append(i+1)
                
        return res