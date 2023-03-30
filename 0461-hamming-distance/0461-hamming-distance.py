class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        res = 0
        while x and y:
            res += (y & 1) ^ (x & 1)
            y = y >> 1
            x = x >> 1
    
        while x:
            res += (x & 1)
            x = x >> 1
            
        while y:
            res += (y & 1)
            y = y >> 1
            
        return res