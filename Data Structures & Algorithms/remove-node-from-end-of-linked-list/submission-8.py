# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        while n > 0:
            first = first.next
            n -= 1
        
        second = head
        ptr = ListNode()
        dummy = ptr
        ptr.next = second
        while first:
            # print(first.val, second.val)
            first = first.next
            second = second.next
            ptr = ptr.next
        ptr.next = ptr.next.next
        return dummy.next