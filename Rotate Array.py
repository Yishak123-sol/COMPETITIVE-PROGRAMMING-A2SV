class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            pop_element = nums.pop()
            nums.insert(0, pop_element)
        
        return nums
