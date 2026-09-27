# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        before = dummy

        # Move to the node before `left`
        for _ in range(left - 1):
            before = before.next

        # Original left node becomes the tail after reversal
        reverse_tail = before.next

        prev = None
        curr = reverse_tail

        reverse_cnt = right - left + 1

        while curr and reverse_cnt > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            reverse_cnt -= 1

        # Connect left side to reversed head
        before.next = prev

        # Connect reversed tail to right side
        reverse_tail.next = curr

        return dummy.next
        

        