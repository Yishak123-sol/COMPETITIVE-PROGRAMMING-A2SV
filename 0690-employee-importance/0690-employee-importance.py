"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.ans = 0
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        visited = set()
        graph = defaultdict(list)
        importance = defaultdict(int)
        for i in range(len(employees)):
            graph[employees[i].id] = employees[i].subordinates
            importance[employees[i].id] = int(employees[i].importance)
                
        
        for i in range(len(employees)):
            if employees[i].id == id:
                return self.dfs(id, employees, graph, visited, importance)
                
    def dfs(self, node, employees, graph, visited, importance):
        
        self.ans += importance[node]
        visited.add(node)
        for employee in graph[node]:
            if employee not in visited:
                self.dfs(employee, employees, graph, visited,importance)
        
        return self.ans