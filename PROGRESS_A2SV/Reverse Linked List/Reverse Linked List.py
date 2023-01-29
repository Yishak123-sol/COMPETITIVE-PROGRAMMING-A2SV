class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        next = None
        pre = None

        while current:

            next = current.next
            current.next = pre
            pre = current
            current = next
        
        return pre 
