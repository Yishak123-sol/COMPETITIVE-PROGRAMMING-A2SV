inp = int(input())
for i in range(inp):
    row = list(map(int, input().split()))
    temp = []
    for j in range(len(row)) :
      if row[j] == 1:
        temp.append(j+1)

    print(len(temp),*temp)
