T = int(input())
for _ in range(T):
    a, b = list(map(int,input().split()))
    min_val = min(a, b)
    max_val = (a+b)//4
    if min_val == 0:
        print(0)
    else:
        print(min(min_val, max_val))
    
