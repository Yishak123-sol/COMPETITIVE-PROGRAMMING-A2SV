"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:return 0
        
        maxdepth = 0
        for node in root.children:
            maxdepth = max(maxdepth, self.dfs(node))
            
        return maxdepth + 1
        
    
            