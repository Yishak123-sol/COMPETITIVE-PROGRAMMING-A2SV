"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)
        importance = defaultdict(int)
        for i in range(len(employees)):
            graph[employees[i].id] = employees[i].subordinates
            importance[employees[i].id] = int(employees[i].importance)
        
        for i in range(len(employees)):
            if employees[i].id == id:
                return self.dfs(id, employees, graph, importance)
                
    def dfs(self, node, employees, graph, importance):
        return (importance[node] + sum(self.dfs(employee, employees, graph, importance) for employee in graph[node]))
        
        