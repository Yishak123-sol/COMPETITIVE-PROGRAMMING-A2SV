class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], als: List[List[int]]) -> int:
        n = len(source)
        p = [i for i in range(n)]
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        idx = set()
        for x,y in als:
            p1,p2 = find(x), find(y)
            idx.add(x)
            idx.add(y)
            if p1 != p2:
                p[p2] = p1
                
        ct = collections.defaultdict(set)
        for node in idx:
            pnode = find(node)
            ct[pnode].add(node)
            ct[pnode].add(pnode)
            
        ans = 0
        for key in ct:
            nodes = ct[key]
            s1 = Counter([source[node] for node in nodes])
            s2 = Counter([target[node] for node in nodes])
            for node in s1:
                if s2[node] < s1[node]:
                    ans += s1[node] - s2[node]
        
        for i in range(n):
            if i not in idx:
                if source[i] != target[i]:
                    ans += 1
                    
        return ans