class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        for key, value in edges:
            graph[key].append(value)
            graph[value].append(key)
            
        """
        {0: [1, 2], 1: [0, 2], 2: [1, 0]}
        
        """
        if source == destination:return True
        stack = []
        visited = set()
        stack.append(graph[source])
        visited.add(source)
        
        while stack:
            curr = stack.pop()
            for vertice in curr:
                if vertice == destination:
                    return True
                
                if vertice not in visited:
                    visited.add(vertice)
                    stack.append(graph[vertice])
                
        return False


        
        
    
        
        
            