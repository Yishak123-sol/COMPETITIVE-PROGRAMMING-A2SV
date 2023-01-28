class MyLinkedList:
    def __init__(self):
        self.isnil = True
        self.val = None
        self.next = None

    def get(self, index):
        if self.isnil:
            return -1
        elif index == 0:
            return self.val
        else:
            return self.next.get(index-1)

    def addAtHead(self, val):
        if self.isnil:
            self.val = val
            self.next = MyLinkedList()
            self.isnil = False
        else:
            new = MyLinkedList()
            new.isnil = False
            new.val = self.val
            new.next= self.next
            self.val = val
            self.next = new    

    def addAtTail(self, val):
        if self.isnil:
            self.addAtHead(val)
        else:
            self.next.addAtTail(val)

    def addAtIndex(self, index, val):
        if self.isnil and index>0:
            return
        elif index == 0:
            self.addAtHead(val)
        else:
            self.next.addAtIndex(index-1,val)

    def deleteAtIndex(self, index):
        if self.isnil:
            return
        elif index == 0:
            if self.next.isnil:
                self.next = None
                self.isnil = True
            else:
                self.val = self.next.val
                self.next = self.next.next
        else:
            self.next.deleteAtIndex(index-1)
