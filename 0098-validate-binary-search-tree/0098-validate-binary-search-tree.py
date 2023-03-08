# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current = root
        stack = []
        visited = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            popped = stack.pop()
            if visited:
                if visited[-1].val >= popped.val: return False
            visited.append(popped)
            current = popped.right
        
        return True
    