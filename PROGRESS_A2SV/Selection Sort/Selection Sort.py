class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            
        return arr