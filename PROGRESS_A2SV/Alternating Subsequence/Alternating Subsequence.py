test_case = int(input())

for _ in range(test_case):
    
    length = int(input())

    arr = list(map(int, input().split()))
    stack = []

    for i in range(length):

        if not stack or (stack[-1] < 0 and arr[i] > 0) or (stack[-1] > 0 and arr[i] < 0):
            stack.append(arr[i])
        
        elif stack and stack[-1] > 0 and arr[i] > 0 and arr[i] > stack[-1]:
            stack.pop()
            stack.append(arr[i])
        
        elif stack and stack[-1] < 0 and arr[i] < 0 and arr[i] > stack[-1]:
            stack.pop()
            stack.append(arr[i])


    print(sum(stack))
