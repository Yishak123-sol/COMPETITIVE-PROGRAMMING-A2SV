class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        if not grid:return True
        
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        
        visited = set()
        return self.depth_firstSearch(0, 0, grid, visited, directions)
    
    def depth_firstSearch(self, r, c, grid, visited, directions):
        
        if r == len(grid)-1 and c == len(grid[0])-1:return True
        visited.add((r, c))
        
        for vertice in directions[grid[r][c]]:
            row, col = vertice[0]+r, vertice[1]+c
            
            if self.inbound(row, col, grid) and (row, col) not in visited and (-vertice[0], -vertice[1]) in directions[grid[row][col]]:
                if self.depth_firstSearch(row, col, grid, visited, directions):
                    return True
        return False
    
    def inbound(self, r, c, grid):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])