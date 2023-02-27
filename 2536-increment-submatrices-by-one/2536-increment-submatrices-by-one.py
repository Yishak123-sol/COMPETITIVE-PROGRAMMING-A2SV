class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        
        mat = [[0 for i in range (n)] for i in range(n) ]
        
        for i in q:
            tr = i[0]
            tc = i[1]
            br = i[2]
            bc = i[3]
            
            mat[tr][tc] += 1
            if br + 1 < n:
                mat[br + 1][tc] -= 1
            if bc + 1 < n:
                mat[tr][bc + 1] -= 1
            if bc + 1 < n and br + 1 < n:
                mat[br + 1][bc + 1] += 1
                
        for row in range(n):
            for col in range(1, n):
                mat[row][col] += mat[row][col-1]
                
        for col in range(n):
            for row in range(1, n):
                mat[row][col] += mat[row-1][col]
                
        
        return mat