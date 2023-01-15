class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        col = len(grid[0])
        row = len(grid)
        count = 0

        if col < 3 or row < 3:
            return count
        
        for j in range(row-2):
            for i in range(col-2):
                
                grid1 = grid[j][i:i+3]
                grid2 = grid[j+1][i:i+3]
                grid3 = grid[j+2][i:i+3]

                if self.is_row_col_diagonal_HaveEquallSum(grid1, grid2, grid3):
                    if self.is_distinct_AND_ONE_upto_Nine(grid1, grid2, grid3):
                        count += 1

        return count


    def is_row_col_diagonal_HaveEquallSum(self, grid1, grid2, grid3):


        row1 = grid1[0] + grid1[1] + grid1[2]
        row2 = grid2[0] + grid2[1] + grid2[2]
        row3 = grid3[0] + grid3[1] + grid3[2]

        col1 = grid1[0] + grid2[0] + grid3[0]
        col2 = grid1[1] + grid2[1] + grid3[1]
        col3 = grid1[2] + grid2[2] + grid3[2]

        diagonal_1 = grid1[0] + grid2[1] + grid3[2]
        diagonal_2 = grid1[0] + grid2[1] + grid3[2]

        if row1 == row2 and row3 == row2 and row3 == col1 and col1 == col2:
            if col2 == col3 and col3 == diagonal_1 and diagonal_1 == diagonal_2:
                return True

        else:
            return False

    def is_distinct_AND_ONE_upto_Nine(self, grid1, grid2, grid3):

        grid_set = set()
        check_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        for i in range(len(grid1)):
            grid_set.add(grid1[i])
        
        for i in range(len(grid2)):
            grid_set.add(grid2[i])

        for i in range(len(grid3)):
            grid_set.add(grid3[i])
        
        print(grid_set)


        return True if grid_set == check_set  else False
             
