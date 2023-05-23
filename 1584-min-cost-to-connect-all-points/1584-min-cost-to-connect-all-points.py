class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distances = []
        n = len(points)
        for i in range(n-1):
            minval = inf
            for j in range(n):
                if j == i:
                    continue
                    
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])      
                distances.append((distance, i, j))
        
        uf = Unionfind(n)
        cost = 0
        distances.sort()
        for distance, i, j in distances:
            if uf.find(i) != uf.find(j):
                cost += distance
                uf.union(i, j)
                
        return cost
                
        
                      
            
class Unionfind:
    def __init__(self, n):
        
        self.root = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
        
    def union(self, x, y):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return
        
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        
        if self.rank[rootx] > self.rank[rooty]: 
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
    
    