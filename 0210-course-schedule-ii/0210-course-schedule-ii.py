class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        course_dependencies = [0] * numCourses
        
        relation_graph = defaultdict(list)
        
        for course, precourse in prerequisites:
            relation_graph[precourse].append(course)
            course_dependencies[course] += 1
        
        
        q = deque()
        for i in range(numCourses):
            if course_dependencies[i] == 0:
                q.append(i)
        

        sorted_array = []
        visited = set()
        while q:
        
            precourse = q.pop()
            sorted_array.append(precourse)
            
            for neighbor in relation_graph[precourse]:
                course_dependencies[neighbor] -= 1
                
                if course_dependencies[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                
        return sorted_array if len(sorted_array) == numCourses else []
        
        