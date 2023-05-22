from collections import defaultdict

_ = int(input())
operation = int(input())
dic = defaultdict(list)

def add(a, b):

    dic[a].append(b)
    dic[b].append(a)

def vert(c):
    if c in dic:
        print(*dic[c])

for i in range(operation):

    li = list(map(int, input().split()))
    if li[0] == 1:
        add(li[1],li[2])

    elif li[0] == 2:
        vert(li[1])
