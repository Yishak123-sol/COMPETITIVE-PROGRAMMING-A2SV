class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        uf = UnionFind(26)
        for eq in equations:
            if eq[1] == "=":
                uf.union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))
        for eq in equations:
            if eq[1] == "!":
                if uf.find(ord(eq[0]) - ord('a')) == uf.find(ord(eq[3]) - ord('a')):
                    return False
        return True
            
        
            
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


    
        