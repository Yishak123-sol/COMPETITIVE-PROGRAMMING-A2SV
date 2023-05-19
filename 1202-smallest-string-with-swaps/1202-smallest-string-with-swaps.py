class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        ob = UnionFind(n)
        
        for i, j in pairs:
            ob.union(i, j)
            
        connected_pairs = defaultdict(list)
        for i in range(n):
            connected_pairs[ob.find(i)].append(i)
        
        ans = list(s)
        for connected in connected_pairs.values():
            chars = sorted([s[i] for i in connected])
            
            for i, char in zip(connected, chars):
                ans[i] = char
                
        ans = "".join(ans)
        
        return ans
            
            
class UnionFind:
    
    def __init__(self, n):
        
        self.root = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            