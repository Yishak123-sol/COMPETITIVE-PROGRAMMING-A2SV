# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        res = [0]
        
        return self.inorder(root, res, count, k)
    
    def inorder(self, root, res, count, k):
    
        if root:
            self.inorder(root.left, res, count, k)
            count[0] += 1
            if k == count[0]:
                res[0] = root.val
            self.inorder(root.right, res, count, k)
            
        return res[0]
          