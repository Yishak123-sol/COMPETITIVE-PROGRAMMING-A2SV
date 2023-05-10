# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:return int(root.val)
        path = ""
        self.dfs(root, str(root.val))
        
        return self.total
    
    def dfs(self, root, path):
        right_path = left_path = 0
        if not root.left and not root.right:return int(path)
        
        
        if root.left:
            l = path + str(root.left.val)
            left_path = self.dfs(root.left, l)
        if root.right:
            r = path + str(root.right.val)
            right_path = self.dfs(root.right, r)
        
        if left_path and right_path:
            self.total += (left_path + right_path)
            
        elif not right_path and left_path:
            self.total += left_path
            
        elif not left_path and right_path:
            self.total += right_path
            
        
        
        
        
        