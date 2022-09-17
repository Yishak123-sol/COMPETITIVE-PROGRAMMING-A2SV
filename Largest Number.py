class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        for i in range(len(nums) - 1):
            for j in range(1+i, len(nums)):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j]=nums[j], nums[i]
        
        answer = "".join(nums)
        if answer == "0" * len(nums):
            return "0"
        else:
            return answer
