# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 1
        root.val = 0
        q = deque([root])
        
        while q:
            
            if len(q) > 1:
                res = max(res, q[-1].val - q[0].val + 1)
                
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    node.left.val = node.val * 2
                    q.append(node.left)
                    
                if node.right:
                    node.right.val = (node.val * 2) + 1
                    q.append(node.right)
                        
        return res