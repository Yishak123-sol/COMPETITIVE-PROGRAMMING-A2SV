class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic_count = Counter(nums)
        sL = []
        count = 0
        for i, j in sorted(dic_count.items()):
            sL.append(j)
            if j > 1:
                for i in range(1, j):
                    count += i
            
        return count
