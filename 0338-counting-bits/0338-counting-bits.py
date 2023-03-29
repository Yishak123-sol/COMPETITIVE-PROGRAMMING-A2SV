class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count_one = 0
            count_one += (i&1) 
            while i > 0:
                count_one += (i >> 1 & 1)
                i = i >> 1
            ans.append(count_one)
                
        return ans
            