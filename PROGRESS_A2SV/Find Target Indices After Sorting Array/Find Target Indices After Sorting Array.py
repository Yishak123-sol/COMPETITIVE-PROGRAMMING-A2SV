class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        count_min = 0
        count_target = 0

        for i in range(len(nums)):
            if nums[i] == target:
                count_target += 1
            elif nums[i] < target:
                count_min += 1

        length = count_min + count_target
        target_indices = []

        for index in range(count_min, length):
            target_indices.append(index)
            

        return target_indices
