# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.same_level = defaultdict(list)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        same_level = self.sameLevel(root, 0)
        if not same_level:return same_level
        return same_level.values()
    
    def sameLevel(self, root, row):
        if not root:return
        
        self.same_level[row].append(root.val)
        self.sameLevel(root.left, row+1)
        self.sameLevel(root.right, row+1)
        
        return self.same_level