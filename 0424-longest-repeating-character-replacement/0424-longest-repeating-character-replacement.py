class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for i in range(ord('A'), ord('Z')+1):
            
            letter = chr(i)
            operation = k
            l = 0
            for r in range(len(s)):
                    
                while l <= r and not operation and s[r] != letter:
                    if s[l] != letter:
                        operation += 1
                    l += 1
            
                if letter != s[r]:
                    operation -= 1
                    
                ans = max(ans, r-l+1)
                        
        return ans
                        