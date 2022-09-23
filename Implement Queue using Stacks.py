class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        
        
    def pop(self) -> int:
        self.creat_queue()
        return self.queue.pop()
    
    
    def peek(self) -> int:
        self.creat_queue()
        return self.queue[-1]

    
    def empty(self) -> bool:
        return not self.stack and not self.queue
        
        
    def creat_queue(self):
        if len(self.queue) == 0:
            while self.stack:
                self.queue.append(self.stack.pop())
            
