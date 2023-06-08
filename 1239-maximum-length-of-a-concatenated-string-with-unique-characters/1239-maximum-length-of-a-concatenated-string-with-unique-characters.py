class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.ans = 0
        self.back_track(arr, "",0)
        return self.ans
    
    def back_track(self, arr, res, idx):
        
        if idx == len(arr):
            self.ans = max(self.ans, len(res))
            return
        
        if len(set(arr[idx])) == len(arr[idx]):
            if all( char not in set(res)  for char in arr[idx]):
                self.back_track(arr, res+arr[idx], idx+1)
        self.back_track(arr, res, idx+1)
            

            
            
        
       