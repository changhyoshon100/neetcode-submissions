# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head
        p_f, p_s = first, second
        while second and second.next:
            first = first.next
            second = second.next.next
            # print(second.val)
        
        prev, curr = None, first.next
        first.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        fst, sec = head, prev
        
        while sec:
            tmp1, tmp2 = fst.next, sec.next
            fst.next = sec
            sec.next = tmp1
            fst, sec = tmp1, tmp2