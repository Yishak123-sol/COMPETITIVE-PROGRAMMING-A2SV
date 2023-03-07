class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        visited = []
        curr = root
        
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            if stack and stack[-1].right == None:
                popped = stack.pop()
                visited.append(popped.val)
            elif stack:
                curr = stack[-1].right
                stack[-1].right = None
                
            if not stack:break
        
        return visited
    