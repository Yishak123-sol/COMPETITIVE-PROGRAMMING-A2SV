# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        curr = root
        stack = []
        visited = []
        while True:
            while curr:
                stack.append(curr)
                visited.append(curr.val)
                curr = curr.left
            if not stack:break
            poped = stack.pop()
            curr = poped.right
            
        return visited