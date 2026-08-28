# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, None)
        pointer = ListNode(0, None)
        stack = []
        pointer.next = node
        pointer = pointer.next
        while head:
            stack.append(head.val)
            head = head.next
        
        while stack:
            value = stack.pop()
            pointer.next = ListNode(value, None)
            pointer = pointer.next
        return node.next