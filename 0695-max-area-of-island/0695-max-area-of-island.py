class Solution(object):
    def maxAreaOfIsland(self, grid):
        
        seen = set()
        maxval = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxval = max(maxval, self.area(r, c, seen, grid))
                
        return maxval
    
    def area(self, r, c, seen, grid):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):return 0
        seen.add((r, c))
        
        return (1 + self.area(r+1, c, seen, grid) + self.area(r-1, c, seen, grid) 
                + self.area(r, c-1, seen, grid) + self.area(r, c+1, seen, grid))
    
    
    
    
    
    
    
        
        