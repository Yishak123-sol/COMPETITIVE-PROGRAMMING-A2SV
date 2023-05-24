# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        summable = []
        queue = deque()
        
        total = 0
        queue.append(root)
        while queue:
            
            head = queue.popleft()
            if (head.val % 2) == 0:
                if head.left and head.left.left:
                    total += head.left.left.val
                    
                if head.left and head.left.right:
                    total += head.left.right.val
                    
                if head.right and head.right.left:
                    total += head.right.left.val
                    
                if head.right and head.right.right:
                    total += head.right.right.val
            
            if head.left and head.right:
                queue.append(head.left)
                queue.append(head.right)
                
            if head.left and not head.right:
                queue.append(head.left)
                
            if not head.left and head.right:
                queue.append(head.right)
                
        return total
                
                
        