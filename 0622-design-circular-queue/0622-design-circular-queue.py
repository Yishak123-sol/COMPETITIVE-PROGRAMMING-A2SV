class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True
        
    
    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return True if not self.queue else False

    def isFull(self) -> bool:
        return True if len(self.queue) == self.k else False
            


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()