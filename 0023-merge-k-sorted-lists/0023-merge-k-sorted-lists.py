# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
                
        dummy = temp = ListNode(0)
        
        while heap:
            val = heapq.heappop(heap)
            new_node = ListNode(val)
            temp.next = new_node
            temp = new_node
        temp.next = None
        
        return dummy.next
                
        