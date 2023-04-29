class Solution:
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        stack = []
        stack.append((0, [0]))
        paths = []
        
        while stack:
            
            node, path = stack.pop()
            if node == len(graph)-1:
                paths.append(path)
            else:
                for neighbor in graph[node]:
                    stack.append((neighbor, path+[neighbor]))
                
        return paths