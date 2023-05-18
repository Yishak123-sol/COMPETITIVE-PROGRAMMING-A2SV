class Solution:
        
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        ob = Unionfind(n)
        for _from, _to, weight in roads:
            ob.union(_from, _to, weight)
            
        return ob.getAnswer(ob.find(n))

class Unionfind:
    def __init__(self, n):
        
        self.root = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
        self.min = [inf for _ in range(n+1)]
        
    def union(self, x, y, weight):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            self.min[rootx] = min(self.min[rootx], weight)
            return
        
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        
        if self.rank[rootx] > self.rank[rooty]:
            self.min[rootx] = min(self.min[rootx], self.min[rooty], weight) 
            self.root[rooty] = rootx
        else:
            self.min[rooty] = min(self.min[rootx], self.min[rooty], weight) 
            self.root[rootx] = rooty
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    def getAnswer(self, n):
        return self.min[n]
    
    
    
    
    