class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        direction = [(0, 1),(0,-1),(-1, 0),(1, 0)]
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 4
                    
                    if self.inbound(i, j-1, grid) and grid[i][j-1] == 1:
                        res -= 2

                    if self.inbound(i-1, j, grid) and grid[i-1][j] == 1:
                        res -= 2
        
        return res
    
    def inbound(self, r, c, grid):
        if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
            return True
        else:
            return False
                    
        
        