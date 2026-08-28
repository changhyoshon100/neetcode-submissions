# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head

        while n > 0:
            n -= 1
            curr = curr.next
        
        if not curr:
            return head.next

        ptr = head
        while curr.next:
            curr = curr.next
            ptr = ptr.next
        ptr.next = ptr.next.next
        return head
        
        