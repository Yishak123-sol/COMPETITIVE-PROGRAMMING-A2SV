class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        largest_pair_sum = 0
        nums.sort()
        for i in range(int(len(nums)/2)):
            if nums[i] + nums[-i-1] > largest_pair_sum :
                largest_pair_sum = nums[i] + nums[-i-1]
                
        return largest_pair_sum
