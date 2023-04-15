class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        
        if color == newColor:return image
        self.dfs(sr, sc, row, col, image, newColor, color)

        return image
    
    def dfs(self, r, c, row, col, image, newColor, color):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                self.dfs(r-1, c,row, col, image, newColor, color)
            if r+1 < row:
                self.dfs(r+1, c,row, col, image, newColor, color)
            if c >= 1:
                self.dfs(r, c-1,row, col, image, newColor, color)
            if c+1 < col:
                self.dfs(r, c+1,row, col, image, newColor, color)
    