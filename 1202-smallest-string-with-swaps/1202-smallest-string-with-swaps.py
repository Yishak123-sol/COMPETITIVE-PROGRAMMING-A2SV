class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        from collections import defaultdict
        
        n = len(s)
        uf = UnionFind(n)
        # Build the graph
        for i, j in pairs:
            uf.union(i, j)
            
        groups = defaultdict(list)
        # Group together connected nodes
        for i in range(n):
            groups[uf.find(i)].append(i)
        # Construct the new string
        res = list(s)
        for group in groups.values():
            
            chars = sorted([s[i] for i in group])
            for i, c in zip(group, chars):
                res[i] = c
                
        return ''.join(res)   
        
        

        from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

