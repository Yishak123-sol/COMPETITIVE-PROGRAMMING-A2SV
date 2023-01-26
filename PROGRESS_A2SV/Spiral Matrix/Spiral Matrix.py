class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        self.matrix = matrix
        row, col = 0, 0
        dx, dy= 0, 1
        totalItems = len(matrix) * len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        ans = []
        count = 0


        while len(ans) != totalItems:

            ans.append(matrix[row][col])
            visited.add((row, col))

            if not self.onBoard(row + dx, col + dy) or (row + dx, col + dy) in visited:
                count += 1
                dx, dy = directions[count%4]
                
            row += dx
            col += dy
        
        return ans
    
    def onBoard(self, row, col):
            return 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[0])
