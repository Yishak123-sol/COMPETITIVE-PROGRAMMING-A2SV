class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        arr = [i**2 for i in range(46341)]
        left = 0
        right = 46341-1
        
        while left <= right:

            if arr[left] + arr[right] == c:
                return True

            elif arr[left] + arr[right] > c:
                right -= 1

            else:
                left += 1
        
        return False
