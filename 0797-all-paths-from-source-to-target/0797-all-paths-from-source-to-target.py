from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        queue.append((0, [0]))
        paths = []
        while queue:
            node, path = queue.popleft()
            
            if len(graph)-1 == node:
                paths.append(path)
            else:
                for neighbor in graph[node]:
                    queue.append((neighbor, path + [neighbor]))
                    
        return paths