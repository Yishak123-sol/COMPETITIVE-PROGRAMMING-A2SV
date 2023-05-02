from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        incoming_nodes = set()
        for edge in edges:
            incoming_nodes.add(edge[1])
        
        all_nodes = set(range(n))
        return list(all_nodes - incoming_nodes)
            
            
        
        
    
                
            
        