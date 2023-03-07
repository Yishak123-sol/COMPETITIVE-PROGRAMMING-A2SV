class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.postorder = []
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = self.travers(root)
        return order
        
    def travers(self, root):
        if root:
            self.travers(root.left)
            self.travers(root.right)
            self.postorder.append(root.val)
            
        return self.postorder