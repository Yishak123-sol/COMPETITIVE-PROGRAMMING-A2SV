# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        return self.back_track(root, '')
    
    def back_track(self, root, row):
        if root:
            if not root.left and not root.right:
                row += str(root.val)
                self.ans.append(row)
            
            if root.left:
                self.back_track(root.left, row + str(root.val) + '->')
            
            if root.right:
                self.back_track(root.right, row + str(root.val) + '->')
                
        return self.ans