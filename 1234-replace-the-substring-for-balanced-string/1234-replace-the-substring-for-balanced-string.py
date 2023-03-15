class Solution:
    def balancedString(self, s: str) -> int:
        
        hashmap = Counter(s)
        length = len(s)
        n = length//4
        extra = {}
        
        for key, value in hashmap.items():
            if value > n:
                extra[key] = value-n
                
        if not extra:return 0
        ans = length
        left = 0
        for right in range(length):
            if s[right] in extra:
                extra[s[right]] -= 1
            
            while max(extra.values()) <= 0:
                ans = min(ans, right-left + 1)
                if s[left] in extra:
                    extra[s[left]] += 1
                left += 1
                
        return ans