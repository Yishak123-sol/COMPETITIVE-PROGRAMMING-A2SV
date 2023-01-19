class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_zero = 0
        count_one = 0
        
        for num in nums:
            
            if num == 0:
                count_zero += 1
            
            elif num == 1:
                count_one += 1
            
        
        for index in range(len(nums)):

            if count_zero > 0:
                nums[index] = 0
                count_zero -= 1
            
            elif count_one > 0:
                nums[index] = 1
                count_one -= 1

            else:
                nums[index] = 2
