class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        coloring_grid = [[0 for i in range(n)] for j in range(m)]
        ans = [False]
        
        for r in range(m):
            for c in range(n):
                if coloring_grid[r][c] == 0:
                    if ans[0] == True:return True
                    self.dfs(direction, grid, r, c, coloring_grid, (-1, -1), ans)
        
        return ans[0]
    
    def dfs(self, direction, grid, r, c, coloring_grid, parent, ans):
        
        coloring_grid[r][c] = 1
        node = grid[r][c]
        for x, y in direction:
            
            nr, nc = r+x, c+y
            if self.in_bound(nr, nc, grid) and coloring_grid[nr][nc] == 1 and (nr, nc) != parent and node == grid[nr][nc]:
                ans[0] = True
                break
                
            if self.in_bound(nr, nc, grid) and coloring_grid[nr][nc] == 0 and (nr, nc) != parent and node == grid[nr][nc]:
                self.dfs(direction, grid, nr, nc, coloring_grid, (r, c), ans)
        
        coloring_grid[r][c] = 2
        
        
    def in_bound(self, r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) 
            
    
    
    
