class Solution:
    def splitString(self, s: str) -> bool:
        
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if self.back_track(i+1, val, s):return True
    
    def back_track(self, idx, prev, s):
        
        if idx == len(s):
            return True
        
        for j in range(idx, len(s)):
            val = int(s[idx:j+1])
            if val+1 == prev and self.back_track(j+1, val, s):
                return True
            
        return False