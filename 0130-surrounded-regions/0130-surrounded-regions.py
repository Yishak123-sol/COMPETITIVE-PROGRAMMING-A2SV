class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(board), len(board[0])
        for i in range(col):
            r, c = 0, i
            if board[r][c] == 'O':
                self.dfs(r, c, directions, board, visited)
        
        for j in range(row):
            r, c = j, 0
            if board[r][c] == 'O':
                self.dfs(r, c, directions, board, visited)
            
        for i in range(col):
            r, c = row-1, i
            if board[r][c] == 'O':
                self.dfs(r, c, directions, board, visited)
            
        for j in range(row):
            r, c = j, col-1
            if board[r][c] == 'O':
                self.dfs(r, c, directions, board, visited)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = "X"
        
        return board
    
    def dfs(self, r, c, directions, board, visited):
        
        visited.add((r, c))
        for x, y in directions:
            nr, nc = r+x, c+y
            if self.inbound(nr, nc, board) and (nr, nc) not in visited and board[nr][nc] == 'O':
                self.dfs(nr, nc, directions, board, visited)
                
    def inbound(self, r, c, board):
        return 0 <= r < len(board) and 0 <= c < len(board[0])
        