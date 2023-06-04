class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def backTrack(i, curr):
            if i == len(arr):
                self.res = max(self.res, len(curr))
                return
            
            if len(set(arr[i])) == len(arr[i]):
                if all(c not in curr for c in arr[i]):
                    backTrack(i + 1, curr + arr[i])
                
            backTrack(i + 1, curr)
        
        self.res = 0
        backTrack(0, '')
        return self.res
                