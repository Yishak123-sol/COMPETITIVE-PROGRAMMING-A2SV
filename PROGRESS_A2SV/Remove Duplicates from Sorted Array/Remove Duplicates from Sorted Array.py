class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        holder = 0
        length = len(nums)

        for seeker in range(1, length):

            if nums[seeker] > nums[holder]:
                nums[holder+1] = nums[seeker]
                holder += 1

        return holder + 1
