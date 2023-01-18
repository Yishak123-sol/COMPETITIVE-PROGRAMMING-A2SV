class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        increasing = 0
        index = 1
        length = len(arr)

        while index < length and arr[index] > arr[index-1]:

            index += 1
            increasing += 1

        decreasing = 0
        while index < length and arr[index] < arr[index-1]:
            index += 1
            decreasing += 1

        
        return True if increasing >= 1 and decreasing >= 1 and index == length else False
