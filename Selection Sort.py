class Solution:
    
    def selectionSort(self, arr, n):
        for i in range(n-1):
          min_index = i
          for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                   min_index = j
          arr[i], arr[min_index] = arr[min_index], arr[i]
      
        return arr
      
if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split())
    Soluton.selectionSort(arr, n)
    for i in range(n):
        print(arr[i], end = " ")
    print()
               
        
               
