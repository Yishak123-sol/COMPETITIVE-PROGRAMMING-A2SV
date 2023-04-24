class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
#         n, curr = divmod(n, 2)
#         while n:
#             if curr == n%2:return False
#             n, curr = divmod(n, 2)
            
#         return True
        
        bits = bin(n)
        prev = bits[0]
        for i in range(1, len(bits)):
            if prev == bits[i]:
                return False
            
            prev = bits[i]
        return True
        