class Solution:
    def __init__(self):
        self.ans = 0
        
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
                return 0
            
        else:
            s = self.kthGrammar(n - 1, math.ceil(k/2))

            # s = string[math.ceil(k/2)]
            if k % 2 == 0 and s == 1:
                return 0
            elif k % 2 == 0 and s == 0:
                return 1
            elif k % 2 != 0 and s == 1:
                return 1
            elif k % 2 != 0 and s == 0:
                return 0
        
        self.ans = self.kthGrammar(n, k)
        return self.ans