class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            
            if token == "+":
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(second_num + first_num)
            elif token == "-":
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(second_num - first_num)
            elif token == "*":
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(int(second_num) * int(first_num))
            elif token == "/":
                first_num = stack.pop()
                second_num = stack.pop()
                stack.append(int(second_num / first_num))
            else:
                stack.append(int(token))

        return stack[0]


        