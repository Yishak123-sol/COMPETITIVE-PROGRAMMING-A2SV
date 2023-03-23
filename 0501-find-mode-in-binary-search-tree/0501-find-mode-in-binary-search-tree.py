# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashmap = defaultdict(int)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        count = self.counter(root)
        maxval = max(count.values())
        
        res = []
        for key, value in count.items():
            if maxval == value:
                res.append(key)
                
        return res
    
    def counter(self, root):
        if root:
            self.hashmap[root.val] += 1
            self.findMode(root.left)
            self.findMode(root.right)
            
        return self.hashmap
        