# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorders = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = self.inorder(root)
        return inorder
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.inorders.append(root.val)
            self.inorder(root.right)
            
        return self.inorders