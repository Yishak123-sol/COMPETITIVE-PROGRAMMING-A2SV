# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev_val = float('-inf')
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        if root:
            left_root = self.isValidBST(root.left)
            if self.prev_val >= root.val:return False
            self.prev_val = root.val
            right_root = self.isValidBST(root.right)
            
        return left_root and right_root
    