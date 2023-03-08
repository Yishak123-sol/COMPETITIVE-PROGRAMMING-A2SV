# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:       
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        result = self.valid(root.right, root.left)
        return result
    
    def valid(self, right_root, left_root):
        if not right_root and not left_root:return True
        if not left_root or not right_root:return False
        if right_root.val != left_root.val:return False
        
        case1 = self.valid(right_root.right, left_root.left)
        case2 = self.valid(right_root.left, left_root.right)
        
        return case1 and case2
        
