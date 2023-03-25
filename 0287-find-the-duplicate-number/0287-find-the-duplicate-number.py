class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                duplicate = cur
            nums[cur] = -nums[cur]
            
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
            
        return duplicate