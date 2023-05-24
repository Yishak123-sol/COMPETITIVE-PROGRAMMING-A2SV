class ThroneInheritance:

    def __init__(self, kingName: str):
        
        self.kingName = kingName
        self.connections = defaultdict(list)
        self.deaths = set()
        self.parent = []
        self.ans = []

    def birth(self, parentName: str, childName: str) -> None:
            
        self.connections[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deaths.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        
        ans = self.helper(self.kingName)
        self.ans = []
            
        return ans
    
    def helper(self, node):
        
        if node not in self.deaths:
            self.ans.append(node)
            
        for neighbor in self.connections[node]:
            self.helper(neighbor)
        
        return self.ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()