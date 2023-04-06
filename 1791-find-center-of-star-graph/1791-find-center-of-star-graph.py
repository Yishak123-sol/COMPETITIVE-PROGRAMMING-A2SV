class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        l, r = edges[0]
        for i in range(1, len(edges)):
            if l not in edges[i]:
                return r
            if r not in edges[i]:
                return l