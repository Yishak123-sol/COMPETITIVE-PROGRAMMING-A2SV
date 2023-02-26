class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        Count = 0
        
        for i in range(len(logs)):
            
            if logs[i] == "../" and Count:
                Count -= 1
                
            elif logs[i] != "./" and logs[i] != "../":
                Count += 1
        
        return Count
    
    
    
    
    