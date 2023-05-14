from typing import List
from collections import defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        
        visited = set()
	    for node in range(V):
	        if node not in visited:
	            if self.dfs(node, visited, None):
                    return 1
                    
        return 0
    def dfs(self, node, visited, parent):
        
        if node in visited:return True
        
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor != parent:
                if self.dfs(neighbor, visited, node):
                    return True
	
#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends