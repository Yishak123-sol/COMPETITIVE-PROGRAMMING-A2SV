class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        current = head
        dummy = ListNode(0)
        dummy.next = current
        n = size - n
        
        if size == 1 or n == 0:
            return current.next

        count = 0
        while current:
            if count == n-1:
                current.next = current.next.next
                break

            count += 1
            current = current.next

        return dummy.next
