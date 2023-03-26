class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        length = len(nums)+1
        
        for i in range(1, length+1):
            if i not in hashset:
                return i