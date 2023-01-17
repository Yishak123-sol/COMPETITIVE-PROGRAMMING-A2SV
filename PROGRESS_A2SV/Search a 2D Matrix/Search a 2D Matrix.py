class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        left = 0
        right = (len(matrix[0]) * len(matrix)) - 1 

        while left <= right:

            mid = (right + left) // 2
            current_col = mid % len(matrix[0])
            current_row = mid // len(matrix[0])

            if matrix[current_row][current_col] == target:
                return True
                break
            
            elif matrix[current_row][current_col] > target:
                right = mid - 1

            else:
                left = mid + 1

        else:
            return False
