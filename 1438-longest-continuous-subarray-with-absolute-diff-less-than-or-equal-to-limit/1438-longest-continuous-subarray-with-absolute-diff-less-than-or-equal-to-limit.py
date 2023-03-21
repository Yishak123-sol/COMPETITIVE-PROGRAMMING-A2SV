class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        min_deque = deque()
        max_deque = deque()
        maxval = start = 0
        
        for i in range(len(nums)):
            while min_deque and min_deque[-1] > nums[i]:
                min_deque.pop()
                
            min_deque.append(nums[i])
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
                
            max_deque.append(nums[i])
                
            while max_deque[0] - min_deque[0] > limit:
                num = nums[start]
                if num == max_deque[0]:
                    max_deque.popleft()
                if num == min_deque[0]:
                    min_deque.popleft()
                start += 1
            maxval = max(maxval, i-start+1)
            
        return maxval