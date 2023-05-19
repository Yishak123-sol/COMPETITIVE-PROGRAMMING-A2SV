class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        equivalent = UnionFind()
        for eq in equations:
            if eq[1] == "=":
                equivalent.union(ord(eq[0])-97, ord(eq[3])-97)
                
        for eq in equations:
            if eq[1] == "!":
                if equivalent.find(ord(eq[0])-97) == equivalent.find(ord(eq[3])-97):
                    return False
        return True
    
class UnionFind():
    
    def __init__(self):
        self.root = [i for i in range(26)]
        self.rank = [0 for _ in range(26)]
    
    def union(self, x, y):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx == rooty:
            return 
        
      
        if self.rank[rootx] == self.rank[rooty]:
            self.rank[rootx] += 1
        
        if self.rank[rootx] >= self.rank[rooty]:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
        
    def find(self, x):
        
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
            

            
        