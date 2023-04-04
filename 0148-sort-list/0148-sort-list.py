# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:return head
        
        left, right = self.split(head)
        
        left_half = self.sortList(left)
        right_half = self.sortList(right)
        
        return self.merge(left_half, right_half)
        
    def split(self, head):
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        return head, mid
    
    
    def merge(self, left, right):
    
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
                
            else:
                curr.next = right
                right = right.next
            curr = curr.next
            
        curr.next = left or right
        return dummy.next

    
    
    
    
    
    
    
    
    
    
    
    