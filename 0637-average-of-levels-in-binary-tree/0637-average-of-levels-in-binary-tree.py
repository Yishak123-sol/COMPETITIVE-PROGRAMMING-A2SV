# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque([root])
        ans = []
        while q:
            
            curr_level_total = 0
            length = len(q)
            
            for _ in range(length):
                
                node = q.popleft()
                curr_level_total += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            ans.append(curr_level_total/length)
            
        return ans