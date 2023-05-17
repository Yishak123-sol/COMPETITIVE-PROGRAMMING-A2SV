from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for edge in edges:
            u, v = edge
            if not uf.union(u, v):
                return edge

        return []
        
        
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return False
        
        self.parent[px] = py
        return True


        