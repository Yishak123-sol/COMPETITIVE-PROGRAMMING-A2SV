class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        hashmap = {0:1}
        total = 0
        count = 0

        for i in range(len(nums)):

            total += nums[i]
            value = (total % k)

            if value in hashmap:
                count += hashmap[value]

            if value in hashmap:
                hashmap[value] += 1

            else:
                hashmap[value] = 1

        return count
