class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        offset = 10**4
        count = [0 for i in range(2*(offset)+1)]
        for num in nums:
            count[offset +num] += 1
        
        for i in range(len(count)-1, -1, -1):
            if count[i] > 0:
                k -= count[i]  
            if k <=0:
                return i-offset
        