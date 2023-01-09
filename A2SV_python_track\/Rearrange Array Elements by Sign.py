class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        rearranged_nums = [0]*len(nums)
        positive_nums_index = 0
        negative_nums_index = 1

        for index in range(len(nums)):

            if nums[index] > 0:
                rearranged_nums[positive_nums_index] = nums[index]
                positive_nums_index += 2

            else:
                rearranged_nums[negative_nums_index] = nums[index]
                negative_nums_index += 2
                
        return rearranged_nums
