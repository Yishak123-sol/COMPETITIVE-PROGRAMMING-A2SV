class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxval = -1

        for i in range(m-2):
            for j in range(n-2):
                total = (grid[i][j] + grid[i][j+1] + grid[i][j+2]) + (grid[i+1][j+1]) + (grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])
                maxval = max(total, maxval)
        
        return maxval
