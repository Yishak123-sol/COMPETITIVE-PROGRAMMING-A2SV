class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        elif head and not head.next or k == 0:
            return head
        
        
    
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length > k:
            head_index = length - k - 1
        else:
            head_index = length - (k % length)-1

        if length == k or length == head_index + 1:
            return head

        current = head
        while head_index:
            head_index -= 1
            current = current.next

        new_head = current.next
        temp = new_head
        current.next = None
        

        while new_head and new_head.next:
            new_head = new_head.next

        new_head.next = head

        return tempv
