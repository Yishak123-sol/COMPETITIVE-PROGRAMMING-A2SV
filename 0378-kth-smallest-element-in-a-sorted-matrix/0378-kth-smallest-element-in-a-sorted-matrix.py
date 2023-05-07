class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        nums = []
        for lists in matrix:
            nums.extend(lists)
            
        heapq.heapify(nums)
        
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        
        return nums[0]