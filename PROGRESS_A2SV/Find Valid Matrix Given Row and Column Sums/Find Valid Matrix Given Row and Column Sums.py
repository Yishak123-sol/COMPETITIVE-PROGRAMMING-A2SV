class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        row = len(rowSum)
        col = len(colSum)

        matrix = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):

                minval = min(colSum[j], rowSum[i])
                if minval > 0:

                    matrix[i][j] = minval
                    colSum[j] -= minval
                    rowSum[i] -= minval
        
        return matrix
