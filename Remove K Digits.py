class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        stack = []
        
        for i in num:
            while stack and k>0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
        stack = stack[:len(stack)-k]
        answer = "".join(stack)
        
        if answer:
            return str(int(answer))
        else:
            return "0"
        
