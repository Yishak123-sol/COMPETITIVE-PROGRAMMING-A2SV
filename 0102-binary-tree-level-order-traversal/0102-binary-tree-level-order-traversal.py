# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return []
        queue = deque([root])
        while queue:
            cur_level = []
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length -= 1
                
            self.ans.append(cur_level)
      
        return self.ans