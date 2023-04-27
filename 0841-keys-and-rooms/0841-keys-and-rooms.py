class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = [False for i in range(len(rooms))]
        
        graph = defaultdict(list)
        
        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
        
        
        q = deque()
        q.append(0)
        
        while q:
            length = len(q)
            for _ in range(length):
                curr_room = q.popleft()
                if visited[curr_room] == False:
                    q.extend(graph[curr_room])
                    visited[curr_room] = True
        
        for key in visited:
            if not key:
                return False
            
        return True
                
            