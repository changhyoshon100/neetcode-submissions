# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = list1
        c2 = list2
        ptr = ListNode(0)
        dummy = ptr
        while c1 and c2:
            if c1.val < c2.val:
                ptr.next = ListNode(c1.val)
                ptr = ptr.next
                c1 = c1.next
            else:
                ptr.next = ListNode(c2.val)
                ptr = ptr.next
                c2 = c2.next
        
        while c1 or c2:
            if c1:
                ptr.next = c1
                ptr = ptr.next
                c1 = c1.next
            else:
                ptr.next = c2
                ptr = ptr.next
                c2 = c2.next

        return dummy.next
                


