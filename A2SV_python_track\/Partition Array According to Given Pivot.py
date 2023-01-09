class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less = []
        equall = []
        greater = []

        for i in range(len(nums)):

            if nums[i] > pivot:
                greater.append(nums[i])

            elif nums[i] < pivot:
                less.append(nums[i])

            else:
                equall.append(nums[i])

        rearranged_num = less + equall + greater

                
        return rearranged_num
