# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.reverse()
        node = ListNode(0)
        first = node
        for val in arr:
            node.next = ListNode(val)
            node = node.next
        
        return first.next