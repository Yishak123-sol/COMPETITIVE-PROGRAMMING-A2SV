# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        temp = None
        curr = root
        node = TreeNode(val)
        
        while curr:
            temp = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
                
        if not temp: return node
        
        if temp.val > val:
            temp.left = node
        else:temp.right = node
        
        return root