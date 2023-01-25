class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        row = len(grid)
        ans = []

        for i in range(row-2):
            temp = []
            for j in range(row-2):
                max_val = max(max(grid[i][j:j+3]), max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3]))
                temp.append(max_val)

            ans.append(temp)

        return ans

