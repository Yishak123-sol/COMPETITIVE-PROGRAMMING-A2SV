class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row = len(matrix)
        column = len(matrix[0])
        ans = []
        for c in range(column):
            newRow = []
            for r in range(row):
                newRow.append(matrix[r][c])
            ans.append(newRow)
            
        return ans
