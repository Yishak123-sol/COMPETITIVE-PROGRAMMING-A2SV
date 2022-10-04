class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_ = 0
        dic = {0:1}
        for num in nums:
            sum_ += num
            if sum_ - k in dic:
                count += dic[sum_-k]
            if sum_ not in dic:
                dic[sum_] = 1
            else:
                dic[sum_] += 1 
                
                
        return count
      
"""
def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            sum_= sum(nums[i:j])
            if sum_ == k:
                count += 1

    return count
 """
