class Solution:
  
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        self.board = board

        if self.column_check() and self.row_check():

            return True if self.three_by_three() else False

        else:
            return False


    def column_check(self):

        for col in range(9):

            check_set = set()

            for row in range(9):

                if self.board[col][row] in check_set:
                    return False
                
                if self.board[col][row] != ".":
                    if int(self.board[col][row]) > 9:
                        return False
            
                if self.board[col][row] != ".":
                    check_set.add(self.board[col][row])

        return True


      
    def row_check(self):

        for row in range(9):

            check_set = set()

            for col in range(9):

                if self.board[row][col] in check_set:
                    return False
                
                if self.board[row][col] != ".":
                        if int(self.board[row][col]) > 9:
                            return False
                
                if self.board[row][col] != ".":
                    check_set.add(self.board[row][col])

        return True


    def three_by_three(self):

        for row in range(0, 9-2, 3):

            row1 = self.board[row][:3] + self.board[row + 1][:3] + self.board[row + 2][:3]
            row2 = self.board[row][3:6] + self.board[row + 1][3:6] + self.board[row + 2][3:6]
            row3 = self.board[row][6:] + self.board[row + 1][6:] + self.board[row + 2][6:]


            grid = [row1, row2, row3]

            for index in range(3):

                check_set = set()

                for i in range(9):

                    if grid[index][i] in check_set:
                        return False
                    
                    if grid[index][i] != ".":
                        if int(grid[index][i]) > 9:

                            return False
                    
                    if grid[index][i] != ".":
                        check_set.add(grid[index][i])


        return True
