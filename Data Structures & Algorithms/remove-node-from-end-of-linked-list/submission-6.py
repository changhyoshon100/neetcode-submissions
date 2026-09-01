# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        while curr and n >= 1:
            curr = curr.next
            n -= 1
        
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        
        while curr:
            curr = curr.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        return ptr.next

