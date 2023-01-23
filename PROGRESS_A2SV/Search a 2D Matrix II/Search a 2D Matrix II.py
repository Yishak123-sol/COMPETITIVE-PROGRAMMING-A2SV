class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        col = len(matrix[0])
        row = len(matrix)

        for i in range(row):

            left = 0
            right = col - 1

            if matrix[i][0] <= target and matrix[i][col-1] >= target:

                while left <= right:

                    mid = right + left // 2

                    if matrix[i][mid] == target:
                        return True
                        break
                    
                    elif matrix[i][mid] > target:
                        right = mid - 1

                    else:
                        left = mid + 1


        return False
