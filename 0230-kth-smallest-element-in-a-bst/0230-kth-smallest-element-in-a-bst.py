# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current  = current.left
            
            if k > 1:
                popped = stack.pop()
                k -= 1
                current = popped.right
            else:
                return stack.pop().val
            
            