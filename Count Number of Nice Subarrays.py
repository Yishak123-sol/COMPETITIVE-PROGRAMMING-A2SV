class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
            count = 0
            sum_ = 0
            dic = {0:1}
            for i in range(len(nums)):
                if nums[i]%2 == 0:
                    nums[i] = 0
                else:
                    nums[i] = 1
                    
                sum_ += nums[i]
                if sum_ - k in dic:
                    count += dic[sum_-k]
                    
                if sum_ not in dic:
                    dic[sum_] = 1
                else:
                    dic[sum_] += 1 
                
            return count
