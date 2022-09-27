class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        i, j = 0, 1
        max_, min_= nums[0], nums[0]
        count = 1

        while i <= j and j < len(nums):
            max_ = max(max_, nums[j])
            min_ = min(min_, nums[j])
            print(max_, min_)


            if max_ - min_ <= limit:
                count = max(count, j - i + 1)

            else:
                if nums[i] == max_:
                    max_ = max(nums[i+1:j + 1]) 
                if nums[i] == min_:
                    min_ = min(nums[i+1:j + 1])
                i += 1

            j += 1

        return count
