class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = [0]*len(nums)
        i = 0
        j = 1

        for s in range(len(nums)):

            if nums[s] > 0:
                ans[i] = nums[s]
                i += 2

            if nums[s] < 0:
                ans[j] = nums[s]
                j += 2
                
        return ans
