class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                pop_character = stack.pop()
                while pop_character != "(":
                    queue.append(pop_character)
                    pop_character = stack.pop()
                stack.extend(queue)
                queue.clear()
        
        answer = "".join(stack)
        
        return answer
                
