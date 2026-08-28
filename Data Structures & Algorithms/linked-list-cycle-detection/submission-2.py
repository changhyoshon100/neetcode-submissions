# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        visit = set()
        while ptr:
            visit.add(ptr)
            ptr = ptr.next
            if ptr in visit:
                return True
        return False