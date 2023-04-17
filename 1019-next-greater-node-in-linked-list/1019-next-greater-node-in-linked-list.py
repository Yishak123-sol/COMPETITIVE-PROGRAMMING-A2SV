# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
            
        result = [0]*length
        stack = []
        curr = head
        i = 0
        
        while curr:
            while stack and stack[-1][0] < curr.val:
                value, index = stack.pop()
                result[index] = curr.val
                
            stack.append((curr.val, i))
            curr = curr.next
            i += 1
            
        return result
        