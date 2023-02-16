# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr_1 = list1
        curr_2 = list2
        dummy = head = ListNode(0)

        while curr_1 and curr_2:

            if curr_1 and curr_2 and curr_1.val < curr_2.val:
                head.next = curr_1
                head = curr_1
                curr_1 = curr_1.next

            else:
                head.next = curr_2
                head = curr_2
                curr_2 = curr_2.next

        
        while curr_1:
            head.next = curr_1
            head = curr_1
            curr_1 = curr_1.next
        
        while curr_2:
            head.next = curr_2
            head = curr_2
            curr_2 = curr_2.next
    
        head.next = None

        return dummy.next
