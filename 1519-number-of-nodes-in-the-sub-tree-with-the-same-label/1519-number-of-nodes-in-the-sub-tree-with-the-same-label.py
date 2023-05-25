
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited = set()
        self.ans = [0] * n
        
        self.dfs(0, graph, visited, labels)
        return self.ans
    
    def dfs(self, node, graph, visited, labels):

        visited.add(node)
        counts = defaultdict(int)
        counts[labels[node]] += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                neighbor_counts = self.dfs(neighbor, graph, visited, labels)
                for label, count in neighbor_counts.items():
                    counts[label] += count
                    
        self.ans[node] = counts[labels[node]]
        return counts
        
        