# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float('-inf')
        high = float('inf')
        return self.valid(root, low, high)
    
    def valid(self, root, low, high):
        if not root:return True
        if root.val <= low or root.val >= high:return False
        
        return self.valid(root.right, root.val, high) and self.valid(root.left, low, root.val)