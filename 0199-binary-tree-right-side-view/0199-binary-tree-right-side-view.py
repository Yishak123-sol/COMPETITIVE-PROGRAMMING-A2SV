# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.right_most = defaultdict(list)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res = self.rightside(0, root)
        ans = []
        for key, value in res.items():
            ans.append(value[-1])
        return ans
    
    def rightside(self, row, root):
        if not root:return 
        
        self.right_most[row].append(root.val)
        self.rightside(row+1, root.left)
        self.rightside(row+1, root.right)
        
        return self.right_most