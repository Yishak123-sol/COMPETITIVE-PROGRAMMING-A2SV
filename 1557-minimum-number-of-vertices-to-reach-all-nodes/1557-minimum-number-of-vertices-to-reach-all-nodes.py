from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        temp = [False]*n
        for idx in range(len(edges)):
            node, neighbor = edges[idx]
            temp[neighbor] = True
        
        ans = []
        for i in range(n):
            if not temp[i]:
                ans.append(i)
                
        return ans
            
            
        
        
    
                
            
        