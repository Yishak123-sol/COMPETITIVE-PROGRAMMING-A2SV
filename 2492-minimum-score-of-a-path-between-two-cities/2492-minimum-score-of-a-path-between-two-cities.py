class Solution:
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        ob = Unionfind(n)
        for _from, _to, weight in roads:
            ob.union(_from-1, _to-1)
        
        ans = inf
        for _from, _, weight in roads:
            if ob.isconnected(_from-1, n-1):
                ans = min(ans, weight)
                
        return ans

class Unionfind:
    def __init__(self, n):
        
        self.root = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.min = [inf for _ in range(n)]
        
    def union(self, x, y):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return
        
        if self.rank[rootx] == self.rank[rooty]:
            # self.root[rooty] = rootx//''
            self.rank[rootx] += 1
        
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
            
        
    def find(self, x):
        
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def isconnected(self, _from, n):
        return self.find(_from) == self.find(n)
    
    
    
    