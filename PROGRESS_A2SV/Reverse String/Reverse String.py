class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s)-1

        while left < right:

            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1


        return s
