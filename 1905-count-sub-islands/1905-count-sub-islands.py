class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited and grid2[i][j] == 1:
                    island = set()
                    self.dfs(i, j, visited, island, grid2, directions)
                    
                    for r, c in island:
                        if grid1[r][c] != 1:
                            break
                    else:
                        count += 1
                    
        return count
    
    def dfs(self, r, c, visited, island, grid, directions):
        
        visited.add((r, c))
        island.add((r, c))
        
        for x, y in directions:
            
            nr, nc = r + x, c + y
            if (nr, nc) not in visited and self.inbound(nr, nc, grid) and grid[nr][nc] == 1:
                self.dfs(nr, nc, visited, island, grid, directions)
    
    
    
    
    def inbound(self, r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])