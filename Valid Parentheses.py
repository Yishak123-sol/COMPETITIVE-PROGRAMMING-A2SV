class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = "({["
        for i in s:
            if i in open_brackets:
                stack.append(i)
                
            else:
                if len(stack) == 0:
                    return False
                elif i == ")" and stack.pop() != "(":
                    return False
                elif i == "]" and stack.pop() != "[":
                    return False
                elif i == "}" and stack.pop() != "{":
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
