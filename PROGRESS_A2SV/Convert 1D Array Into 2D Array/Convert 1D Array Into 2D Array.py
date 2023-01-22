class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        row = m
        col = n
        
        if m*n != len(original):
            return []

        matrix = [[0 for i in range(col)] for j in range(row)]
        index = 0

        for i in range(row):
            for j in range(col):
                matrix[i][j] = original[index]
                index += 1

        return matrix
