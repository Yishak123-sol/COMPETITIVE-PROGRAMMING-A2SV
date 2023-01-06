class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        index_store = {}

        for i in range(len(nums)):
                index_store[nums[i]] = i

        for operation in operations:

            index = index_store[operation[0]]
            nums[index] = operation[1]

            del index_store[operation[0]]
            index_store[operation[1]] = index


        return nums
