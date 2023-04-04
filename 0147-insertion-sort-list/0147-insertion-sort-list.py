# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def add_to_sorted_list(self, head, sorted_head, sorted_tail):
            
        if sorted_head == sorted_tail or head.val >= sorted_tail.val:
            sorted_tail.next = head
            head.next = None
            sorted_tail = head
            
        else:
            while sorted_head.next and sorted_head.next.val <= head.val:
                sorted_head = sorted_head.next
                
            head.next = sorted_head.next
            sorted_head.next = head
            
        return sorted_tail

     def insertionSortList(self, head):

        sorted_head = ListNode(None)
        sorted_tail = sorted_head
        while head:
            temp = head.next
            sorted_tail = self.add_to_sorted_list(head, sorted_head, sorted_tail)
            head = temp
            
        return sorted_head.next