class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        
        for char in s:
            if not char.isalnum() or char == " ":
                s = s.replace(char, "")
        
        return True if s == s[::-1] else False
