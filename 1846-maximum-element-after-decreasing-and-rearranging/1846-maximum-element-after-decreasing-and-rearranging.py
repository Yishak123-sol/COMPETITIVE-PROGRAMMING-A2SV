class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
          
        arr.sort()    
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) >= 1:
                arr[i] = arr[i-1] + 1
        
        maxval = max(arr)
        return maxval if maxval <= len(arr) else len(arr)