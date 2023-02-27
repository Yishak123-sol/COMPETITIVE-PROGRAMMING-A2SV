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
            for col in range(n):
                
                top = mat[row - 1][col] if row - 1 >= 0 else 0
                left = mat[row][col - 1] if col - 1 >= 0 else 0
                di = mat[row - 1][col - 1] if col - 1 >= 0 and row - 1 >= 0 else 0
                
                mat[row][col] += top + left - di
        
        return mat