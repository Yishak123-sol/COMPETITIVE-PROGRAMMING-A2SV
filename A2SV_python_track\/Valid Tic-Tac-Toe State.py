class Solution:
    def is_win(self, board, player):
	
        #Check the rows
        for index in range(len(board)):
            if board[index][0] == board[index][1] == board[index][2] == player:
                return True                        

        #Check the columns
        for index in range(len(board)):
            if board[0][index] == board[1][index] == board[2][index] == player:
                return True 
										
        #Check the diagonals
        if board[0][0] == board[1][1] == board[2][2]  == player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
						
        return False

        
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        x_count = 0
        o_count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == "X":
                    x_count += 1

                elif  board[i][j] == "O":
                    o_count += 1
										
        if (o_count > x_count) or (x_count - o_count > 1):
            return False
        
        if self.is_win(board, 'O'):
            if self.is_win(board, 'X'):
                return False

            if (o_count == x_count):
                return True

            else:
                return False
        
        if self.is_win(board, 'X') and x_count != o_count + 1:
            return False

        return True



        
