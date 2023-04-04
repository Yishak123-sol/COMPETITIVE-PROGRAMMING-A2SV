# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:return head
        
        left, right = self.split(head)
        left_half = self.insertionSortList(left)
        right_half = self.insertionSortList(right)
        
        return self.merge(left_half, right_half)
    
    def split(self, head):
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        return head, mid
    
    def merge(self, left_half, right_half):
        
        dummy = ListNode(0)
        curr = dummy
        while left_half and right_half:
            
            if left_half.val < right_half.val:
                curr.next = left_half
                left_half = left_half.next
                
            else:
                curr.next = right_half
                right_half = right_half.next
            curr =  curr.next
            
        curr.next = right_half or left_half
        
        return dummy.next
                
                
        