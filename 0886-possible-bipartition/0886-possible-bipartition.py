class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for vertex, neighbor in dislikes:
            graph[vertex].append(neighbor)
            graph[neighbor].append(vertex)
        
        self.result = True
        color = [False]*(n+1)
        visited = set()
        
        for vertex, neighbor in dislikes:
            if vertex not in visited:
                self.dfs(vertex, graph, visited, color)
        
        return self.result
        
    def dfs(self,node, graph, visited, color):
        
        if not self.result:return
        
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                color[neighbor] = not color[node]
                self.dfs(neighbor, graph, visited, color)
            else:
                if color[neighbor] == color[node]:
                    self.result = False
                