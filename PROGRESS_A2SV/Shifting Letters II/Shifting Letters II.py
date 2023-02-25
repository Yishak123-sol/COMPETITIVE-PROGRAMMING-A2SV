class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        ans = []
        update = [0] * len(s)
        for i in range(len(shifts)):
            
            left, right, val = shifts[i]
            if val == 0:
                val = -1
            update[left] += val 

            if right+1 < len(s):
                update[right+1] -= val
        su = 0
        for j in range(len(s)):

            su += update[j]
            idx = ord(s[j]) - 97
            index = (97 +(26+idx+(su%26)) %26)
            letter = chr(index)
            update[j] = letter
        
        shifted_string = "".join(update)

        return shifted_string

