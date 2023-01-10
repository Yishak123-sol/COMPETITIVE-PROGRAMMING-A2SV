class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if (num - 3) % 3 != 0:
            return []

        elif (num-3) % 3 == 0:
            num1 = int((num-3) / 3)
            consecutive_integers = [num1, num1+1, num1+2]
            
            return consecutive_integers
