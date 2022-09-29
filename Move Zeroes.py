class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0
        right_pointer = 1
        
        if len(nums) == 1:
            return nums
        
        while left_pointer < len(nums) and right_pointer < len(nums):
            if nums[left_pointer] == 0:
                if nums[right_pointer] != 0:
                    nums[right_pointer], nums[left_pointer] =  nums[left_pointer], nums[right_pointer]
                    right_pointer += 1
                    left_pointer += 1
                
                else:
                    right_pointer += 1
            else:
                right_pointer += 1
                left_pointer += 1
                
        return nums
