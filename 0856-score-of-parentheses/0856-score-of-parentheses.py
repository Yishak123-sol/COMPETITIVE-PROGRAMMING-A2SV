class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
    
        
        stack = [0]  # Start with a base score of 0
        for parenthese in s:
            
            if parenthese == "(":
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * last
        
        return stack[0]
