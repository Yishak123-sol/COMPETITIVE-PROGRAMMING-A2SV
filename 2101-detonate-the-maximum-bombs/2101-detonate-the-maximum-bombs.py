from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                
                distance = ((x1 - x2) **2 + (y1 - y2)**2)
                
                if distance <= r1**2:
                    graph[i].append(j)

                    
        maxval = 0
        for node in range(len(bombs)):
            visited = set()
            maxval = max(maxval, self.dfs(visited, graph, node))
            
        return maxval
    
    def dfs(self, visited, graph, node):
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(visited, graph, neighbor)
                
        return len(visited)
                
                