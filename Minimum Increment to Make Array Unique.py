class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1] += 1
                count += 1
                
            elif nums[i] > nums[i+1]:
                count += (nums[i] - nums[i+1]) + 1
                nums[i+1] += (nums[i] - nums[i+1]) + 1
                

        return count
    
