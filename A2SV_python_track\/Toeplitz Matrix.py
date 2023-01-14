class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        row_indx = 0

        while row_indx < (row-1):
            
            for col_indx in range(col-1):
                if matrix[row_indx][col_indx] != matrix[row_indx+1][col_indx+1]:
                    return False

            row_indx += 1
        
        return True

