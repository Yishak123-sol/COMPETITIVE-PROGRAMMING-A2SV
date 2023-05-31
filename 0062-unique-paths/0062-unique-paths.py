class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        return self.dp(0, 0, memo, m, n)
    
    def dp(self, r, c, memo, m, n):
        
        if r == m-1 and c == n-1:return 1
        
        if r >= m or c >= n:return 0
        
        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = self.dp(r+1, c, memo, m, n) + self.dp(r, c+1, memo, m, n)
        
        return memo[(r, c)]
        
        