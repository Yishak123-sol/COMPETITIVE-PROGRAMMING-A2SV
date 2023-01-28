row, col = list(map(int, input().split()))
grid = [input()  for i in range(row)]
 
def is_inBound(r, c):
    return  0 <= r < row and 0 <= c < col
 
def is_croosword(i, j):
 
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
 
    for dx, dy in directions:
 
        r, c = i+dx, j+dy
 
        while is_inBound(r, c):
 
            if grid[i][j] == grid[r][c]:
                return False
                break
 
            r += dx
            c += dy
    else:
        return True
 
 
ans = []
 
for i in range(row):
    for j in range(col):
        if is_croosword(i, j):
            ans.append(grid[i][j])
 
ans = "".join(ans)
print(ans)
