class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        right = max(nums)
        minval = float('inf')
        left = 1
        while left <= right:
            
            mid = left + (right-left)//2
            total = 0
            for i in range(len(nums)):
                total += math.ceil(nums[i]/mid)
                if total > threshold:
                    break
            if total > threshold:
                left = mid + 1
            else:
                minval = min(minval, mid)
                right = mid - 1
                
                
        return minval