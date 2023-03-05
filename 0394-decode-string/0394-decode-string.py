class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        curr_letters = []
        num = 0
        
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char.isalpha():
                curr_letters.append(char)
            elif char == "[":
                stack.append((num, curr_letters))
                curr_letters = []
                num = 0
            else:
                prev_num, prev_letter = stack.pop()
                curr_letter = "".join(curr_letters)
                curr_letters = [*prev_letter, prev_num * curr_letter]
                
        return "".join(curr_letters)