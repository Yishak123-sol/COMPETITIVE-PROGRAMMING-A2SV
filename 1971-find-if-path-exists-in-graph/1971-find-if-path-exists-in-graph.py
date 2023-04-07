class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for key, value in edges:
            graph[value].append(key)
            graph[key].append(value)

        visited = set()
        return self.DFS(source, visited, graph, destination)
    
    def DFS(self, source, visited, graph, destination):
        if source == destination:return True
        visited.add(source)
        
        if destination in graph[source]:
            return True
        
        for neighbor in graph[source]:
            if neighbor not in visited:
                if self.DFS(neighbor, visited, graph, destination):
                    return True
                
        return False
    
    
        
        
            