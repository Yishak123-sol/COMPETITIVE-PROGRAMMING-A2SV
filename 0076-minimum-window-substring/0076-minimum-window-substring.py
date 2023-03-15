
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = Counter(t)
        required = len(target)
        print(len(s))
        left = formated = 0
        window = defaultdict(int)
        res = (float("inf"), None, None)
        for right in range(len(s)):
            
            window[s[right]] += 1
            if window[s[right]] == target[s[right]]:
                formated += 1
                
            while left <= right and required == formated:
                
                if right - left + 1 < res[0]:
                    res = (right-left+1, left, right)
                    
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    formated -= 1
                
                left += 1
                
        return ""  if res[0] == float("inf") else s[res[1]:res[2]+1]
                
                

        
