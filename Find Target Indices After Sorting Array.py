class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range((len(nums)-1) - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        counting_the_index = []
        count = 0
        
        for check_target in nums:
            if target == check_target:
                index = nums.index(check_target)
                counting_the_index.append(count)
            count += 1

        return(counting_the_index)
