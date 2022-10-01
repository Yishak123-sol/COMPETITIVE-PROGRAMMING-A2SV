class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_count = 0
        left = 0
        for right in range(len(s)):
            if s[right] in s[left:right]:
                while s[right] !=  s[left]:
                    left += 1
                left += 1
                
            max_count = max(max_count, right-left+1)
            
        return max_count
