class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False for i in range(len(rooms))]
        
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
        self.dfs(0, visited, graph)
        for key in visited:
            if not key:
                return False
            
        return True
    def dfs(self, room, visited, graph):
        
        visited[room] = True
        for key in graph[room]:
            if not visited[key]:
                self.dfs(key, visited, graph)
                