class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        del arr[0]
        arr.append(-1)
        left = 0
        
        for left in range(1, len(arr)):

            right = left - 1

            while arr[left] > arr[right] and right >= 0:

                arr[right] = arr[left]
                right -= 1


        return arr
