class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def empty(self) -> bool:
        return True if not self.stack else False


    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()