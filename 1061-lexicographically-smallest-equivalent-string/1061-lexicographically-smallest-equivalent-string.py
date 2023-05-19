class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        ob = UnionFind()
        
        for i in range(len(s1)):
            ob.union(s1[i], s2[i])
        
        ans = ""
        for i in range(len(baseStr)):
            ans += ob.find(baseStr[i])
        
        return ans
            
        
class UnionFind():
    def __init__(self):
        self.root = defaultdict(list)
        
        for i in range(ord('a'), ord('z')+1):
            self.root[chr(i)] = chr(i)
        
    def union(self, x, y):
        
        rootx = self.find(x)
        rooty = self.find(y)
        
        minChar = min(rootx, rooty)
        
        if minChar == rootx:
            self.root[rooty] = rootx
        else:
            self.root[rootx] = rooty
            
    def find(self, x):
        
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
            
        return self.root[x]
