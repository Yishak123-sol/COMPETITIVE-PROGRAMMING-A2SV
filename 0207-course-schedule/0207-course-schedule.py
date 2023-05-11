class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        indegree = [0]*numCourses
        
        for child, par in prerequisites:
            graph[par].append(child)
            indegree[child] += 1
        
        q = deque()
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                print(neighbor)
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
            
        return True if count == numCourses else False
                    
                    