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
        queue = deque()
        queue.append((0, 0))
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            if r == len(grid)-1 and c == len(grid[0])-1:return True
            
            for dx, dy in directions[grid[r][c]]:
                row, col = r+dx, dy+c
                if self.inbound(row, col, grid) and (row, col) not in visited and (-dx, -dy) in directions[grid[row][col]]:
                    queue.append((row, col))
                    
    def inbound(self, r, c, grid):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])