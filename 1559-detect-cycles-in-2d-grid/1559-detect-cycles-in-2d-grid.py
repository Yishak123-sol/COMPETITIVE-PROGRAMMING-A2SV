class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    seen = set()
                    self.dfs(grid, r, c, direction, visited, seen, None)
                    if True in seen:
                        return True
                    
        return False
    
    
    def dfs(self, grid, r, c, direction, visited, seen, parent):
        
        visited.add((r, c))
        seen.add((r, c))
        for x, y in direction:
            nr, nc = r+x, c+y
            if (nr, nc) in seen and (nr, nc) != parent:
                seen.add(True)
                break
                
            if self.is_inbound(nr, nc, grid) and grid[nr][nc] == grid[r][c] and (nr, nc) != parent:
                self.dfs(grid, nr, nc, direction, visited, seen, (r, c))


    def is_inbound(self, r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])