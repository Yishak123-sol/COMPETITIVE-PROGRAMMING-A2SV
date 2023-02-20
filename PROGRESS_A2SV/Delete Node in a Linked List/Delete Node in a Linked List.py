class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        while node and node.next:
            node.val = node.next.val
            temp = node
            node = node.next
        temp.next = None
