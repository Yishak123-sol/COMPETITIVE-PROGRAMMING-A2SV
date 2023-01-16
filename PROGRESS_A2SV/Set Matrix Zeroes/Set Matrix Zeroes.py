class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.matrix = matrix
        zero_position = self.find_zerosPosition(matrix)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for index in range(len(zero_position)):

            for direct_row, direct_col in directions:

                row = zero_position[index][0]
                col = zero_position[index][1]

                while self.is_onBoard(row, col):
                    matrix[row][col] = 0

                    row += direct_row
                    col += direct_col
                            
        return matrix

    def is_onBoard(self, row, col):

        if row > (len(self.matrix)-1) or col > (len(self.matrix[0]) - 1) or row < 0 or col < 0:
            return False
          
        return True
    

    def find_zerosPosition(self, matrix):

        zero_position = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_position.append((row, col))
                    

        return zero_position
      
      
