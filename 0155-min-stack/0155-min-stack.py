class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.minstack and self.minstack[-1] >= val or not self.minstack:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        return popped
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None
    
    
#     def __init__(self):
#         self.minstack = []
#         self.stack = []

#     def push(self, val: int) -> None:
#         if not self.minstack:
#             self.minstack.append(val)
#         else:
#             if self.minstack[-1] >= val:
#                 self.minstack.append(val)
#         self.stack.append(val)

#     def pop(self) -> None:
#         if self.stack:
#             value = self.stack.pop()
#             if value == self.minstack[-1]:
#                 self.minstack.pop()

#     def top(self) -> int:
#         return self.stack[-1] if self.stack else None

#     def getMin(self) -> int:
#         return self.minstack[-1] if self.minstack else None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()