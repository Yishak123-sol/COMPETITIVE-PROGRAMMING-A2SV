class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        most_frequent_to_less = []
        for i, j in nums.most_common(k):
            most_frequent_to_less.append(i)
            
        return most_frequent_to_less
