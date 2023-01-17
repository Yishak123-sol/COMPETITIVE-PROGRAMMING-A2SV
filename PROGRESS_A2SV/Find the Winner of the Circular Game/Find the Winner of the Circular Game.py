class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends_array = [i for i in range(1, n+1)]
        current = 0

        while len(friends_array) > 1:

            current = (current + k - 1) % len(friends_array)
            start = current

            if current == (len(friends_array) - 1):
                start = 0

            del friends_array[current]
            current = start
            

        return friends_array[0]
