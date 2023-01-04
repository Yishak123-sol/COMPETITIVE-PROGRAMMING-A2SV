def is_inboard(row, column):

    if row < 0 or row > 7 or column > 7 or column < 0:
        return False

    return True


def is_queen(row, column, queens):

    for queen in queens:

        if queen == [row, column]:
            return True

    return False


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        position = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        cordinate = []

        for index in range(8):

            row = king[0]
            column = king[1]

            while is_inboard(row, column):

                if is_queen(row, column, queens):
                    cordinate.append([row, column])
                    
                    break
                
                row += position[index][0]
                column += position[index][1]
                

        return cordinate

        
