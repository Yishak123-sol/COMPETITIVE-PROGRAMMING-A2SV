# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        curr = head
        length = 0
        
        while curr:
            curr = curr.next
            length += 1
        
        mid = length // 2
        temp = []
        curr = head
        
        for i in range(mid):
            temp.append(curr.val)
            curr = curr.next
        
        maxval = 0
        j = mid-1
        while curr:
            total = curr.val + temp[j]
            maxval = max(maxval, total)
            curr = curr.next
            j -= 1
            
        return maxval
            
        