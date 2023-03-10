# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = defaultdict(list)
        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxval = 0
        res = self.maxwid(root, 0, 0)
        for key, value in res.items():
            if (len(value)) > 1:
                prev = value[-1]-value[0] + 1
            else:
                prev = 1
            maxval = max(prev, maxval)
        return maxval
    
    def maxwid(self, root, row, index):
        if root:
            self.dic[row].append(index)
            self.maxwid(root.left, row+1, 2*index)
            self.maxwid(root.right, row+1, 2*index+1)
        
        return self.dic
        