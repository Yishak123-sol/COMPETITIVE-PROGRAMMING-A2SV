class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # cur_sum = -math.inf
        # best_sum = -math.inf

        # for num in nums:
        #     cur_sum = max(cur_sum + num, num)
        #     best_sum = max(best_sum, cur_sum)

        # return best_sum


        left_min = math.inf
        cur_prefix = 0
        ans = -math.inf
        for num in nums:
            left_min = min(left_min,cur_prefix)
            cur_prefix += num
            ans = max(ans,cur_prefix - left_min)
            
        return ans
