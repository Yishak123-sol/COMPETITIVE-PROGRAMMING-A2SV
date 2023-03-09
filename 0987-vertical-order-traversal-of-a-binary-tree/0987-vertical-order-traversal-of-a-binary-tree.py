# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.same_col_elements = defaultdict(list)
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        same_col = self.level_order(root, 0, 0)
        same_col = sorted(same_col.items())
        
        row = []
        for col in same_col:
            col = col[1]
            col.sort()
            row.append(col)
            
        result = []
        for col in row:
            ro = []
            for i in range(len(col)):
                ro.append(col[i][1])
            result.append(ro)
            
        return result
        
    def level_order(self, root, row, col):
        if not root:return 
        self.same_col_elements[col].append((row, root.val))
        self.level_order(root.left, row+1, col-1)
        self.level_order(root.right, row+1, col+1)
        
        return self.same_col_elements