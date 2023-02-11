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
            
            
     """ 
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        
        self.head = None
        self.nodes = []
        self.map = {}

    def get(self, index: int) -> int:

        if index > len(self.nodes)-1 or index < 0:
            return -1
        return self.nodes[index].val

    def addAtHead(self, val: int) -> None:

        node = Node(val, self.head)
        self.nodes.insert(0, node)
        self.map[val] = 0

        for i in range(1, len(self.nodes)):
            self.map[self.nodes[i].val] = i
        self.head = node


    def addAtTail(self, val: int) -> None:

        node = Node(val)
        self.nodes.append(node)
        self.map[val] = len(self.nodes)-1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > len(self.nodes) or index < 0:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == len(self.nodes):
            self.addAtTail(val)
        else:
            node = Node(val, self.nodes[index])
            self.nodes.insert(index, node)
            self.map[val] = index

            for i in range(index+1, len(self.nodes)):
                self.map[self.nodes[i]] = i


    def deleteAtIndex(self, index: int) -> None:
        
        if index > len(self.nodes) or index < 0:
            return

        val = self.nodes[index].val
        del self.nodes[index]
        del self.map[val]

        for i in range(index, len(self.nodes)):
            self.map[self.nodes[i]] = i

            """
