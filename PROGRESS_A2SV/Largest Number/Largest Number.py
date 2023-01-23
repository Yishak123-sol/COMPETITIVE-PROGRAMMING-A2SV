class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)-1):

            nums[i] = str(nums[i])

            for j in range(i+1, len(nums)):
                if nums[i] + str(nums[j]) < str(nums[j]) + nums[i]:
                    nums[i], nums[j] = str(nums[j]), nums[i]
                    
                    
        largest_num = "".join(nums)

        return largest_num
