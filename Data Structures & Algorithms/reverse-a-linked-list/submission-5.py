# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        front = node
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        for a in reversed(arr):
            subNode = ListNode(a)
            node.next = subNode
            node = node.next

        return front.next

            

