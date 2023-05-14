class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        indegree = [0]*n
        for nod, nei in edges:
            graph[nod].append(nei)
            indegree[nei] += 1
            
        queue = deque()
        
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)
                
        ans = [set() for i in range(n)]
        while queue:
            
            node = queue.popleft()
            for neighbor in graph[node]:
                
                ans[neighbor].add(node)
                if ans[node]:
                    ans[neighbor].update(ans[node])
                    
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for i in range(n):
            ans[i] = list(ans[i])
            ans[i].sort()
            
        return ans
        
    