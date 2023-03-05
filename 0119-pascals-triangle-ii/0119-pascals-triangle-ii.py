class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        rows = []
        
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(rows[-1][j-1] + rows[-1][j])
            rows.append(row)
        
        return rows[-1]