class Solution:
    def findComplement(self, num: int) -> int:
        
        count = 0
        res = 0
        
        while num > 0:
            val = 1-(num & 1)
            if val == 1:
                res+= 2**(count*val)
            num = num >> 1
            count += 1
        
        return res