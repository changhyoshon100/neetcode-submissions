class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        before = dummy

        # Move to the node before `left`
        for _ in range(left - 1):
            before = before.next

        curr = before.next

        # Move each next node to the front of the reversed section
        for _ in range(right - left):
            move = curr.next
            curr.next = move.next
            move.next = before.next
            before.next = move

        return dummy.next