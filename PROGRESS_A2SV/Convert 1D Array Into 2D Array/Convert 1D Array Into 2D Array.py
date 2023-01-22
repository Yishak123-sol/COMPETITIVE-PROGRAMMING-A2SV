class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n != len(original):
            return []

        matrix = []
        index = 0

        for i in range(m):

            row = []

            for j in range(n):
                row.append(original[index])
                index += 1

            matrix.append(row)

        return matrix
