# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = [0,0]
        self.ans = 0
        self.total = 0
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root:
            node = root
            temp = self.preorder(node)
            if temp == node.val:
                self.ans += 1
            self.count[0] = 0
            self.count[1] = 0
            self.averageOfSubtree(root.left)
            self.averageOfSubtree(root.right)
            
        return self.ans
       
    
    def preorder(self, root):
        if root:
            self.count[0] += 1
            self.count[1] += root.val
            self.preorder(root.left)
            self.preorder(root.right)
        
        return int(self.count[1]/self.count[0]) if self.count[0] > 0 else -1
            
            