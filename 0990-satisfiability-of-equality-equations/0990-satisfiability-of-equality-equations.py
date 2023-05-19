class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        connected = defaultdict(list)
        for equ in equations:
            if equ[1] == '=':
                connected[equ[0]].append(equ[3])
                connected[equ[3]].append(equ[0])
    
        for equ in equations:
            if equ[1] == '!':
                if self.bfs(equ[0], connected, equ[3]):
                    return False
                
        return True
    
    def bfs(self, node, connected, tar):
        
        visited = set()
        queue = deque()
        queue.append(node)
        while queue:
            
            node = queue.popleft()
            if node == tar:return True
            visited.add(node)
            
            for neighbor in connected[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
                if neighbor == tar:return True
                
        return False
            