def longestOnes(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        max_count = 0
        for right_pointer in range(len(nums)):
            if nums[right_pointer] == 0:
                k -= 1
                
            if k < 0:
                k += (1 - nums[left_pointer])
                left_pointer += 1
                
            max_count = max(max_count, right_pointer-left_pointer + 1)
        
        return max_count
