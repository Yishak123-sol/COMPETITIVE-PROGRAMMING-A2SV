class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.full = k
        
    def insertFront(self, value: int) -> bool:
        if self.full > len(self.deque):
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.full > len(self.deque):
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.deque) > 0:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.deque) > 0:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        else:
            False
    def isFull(self) -> bool:
        if len(self.deque) == self.full:
            return True
        else:
            False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
