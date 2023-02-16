t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    l = n+m-1
    matrix = [list(map(int, input().split())) for _ in range(n)]

    diagonal_sums1 = [0 for i in range(l)]
    diagonal_sums2 = [0 for i in range(l)]

    for i in range(n):
        for j in range(m):
            diagonal_sums1[i+j] += matrix[i][j]
            if i-j < 0:
                diagonal_sums2[l+i-j] += matrix[i][j]
            else:
                diagonal_sums2[i-j] += matrix[i][j]


    maxval = 0
    for i in range(n):
        for j in range(m):
            if i-j < 0:
                maxval = max(maxval, diagonal_sums1[i+j] + diagonal_sums2[l+i-j] - matrix[i][j])
            else:
                maxval = max(maxval, diagonal_sums1[i+j] + diagonal_sums2[i-j] - matrix[i][j])

    print(maxval)
