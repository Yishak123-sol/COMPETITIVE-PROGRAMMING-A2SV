# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            self.ans.append(str(root.val))
            if root.left and root.right:
                
                self.ans.append("(")
                self.tree2str(root.left)
                self.ans.append(")")
                
                self.ans.append("(")
                self.tree2str(root.right)
                self.ans.append(")")
                
            if root.left and not root.right:
                self.ans.append("(")
                self.tree2str(root.left)
                self.ans.append(")")
                
            if not root.left and root.right:
                self.ans.append("(")
                self.ans.append(")")
                
                self.ans.append("(")
                self.tree2str(root.right)
                self.ans.append(")")
                
                
        return "".join(self.ans)