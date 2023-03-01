class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        stack = []
        
        for curr in path:
            if curr == "" or curr == ".":
                continue
            elif curr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(curr)
        
        
        ans = "/" + "/".join(stack)
        return ans
    
    
    
    
    
    