
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        hashmap = {0:1}
        total_odd = 0
        nice = 0

        for i in range(len(nums)):

            if nums[i] % 2 != 0:
                total_odd += 1

            if total_odd-k in hashmap:
                nice += hashmap[total_odd-k]
            
            if total_odd in hashmap:
                hashmap[total_odd] += 1

            else:
                hashmap[total_odd] = 1

        return nice


