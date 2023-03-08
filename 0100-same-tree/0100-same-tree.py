# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isValid(p, q)
    
    def isValid(self, p, q):
        if not p and not q:return True
        if not p or not q:return False
        if p.val != q.val:return False
        
        case1 = self.isValid(p.left, q.left)
        case2 = self.isValid(p.right, q.right)
        
        return case1 and case2
    
    