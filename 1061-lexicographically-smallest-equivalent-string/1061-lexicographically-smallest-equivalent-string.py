class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        from collections import defaultdict
        
        graph = defaultdict(list)
        
        for i in range(len(s1)):
            graph[s1[i]].append(s2[i])
            graph[s2[i]].append(s1[i])
        
        minChar = [0]
        ans_holder = ''
        for i in range(len(baseStr)):
            visited = set()
            minChar[0] = baseStr[i]
            self.helper(minChar[0], visited, graph, minChar)
            ans_holder += minChar[0]
            
        return ans_holder
            
    def helper(self, node, visited, graph, minChar):
        
        visited.add(node)
        minChar[0] = min(minChar[0], node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.helper(neighbor, visited, graph, minChar)
        
        
        