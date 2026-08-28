# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = []
        for li in lists:
            while li:
                node.append(li.val)
                li = li.next
        node.sort()

        res = ListNode(0)
        curr = res
        for v in node:
            curr.next = ListNode(v)
            curr = curr.next
        return res.next

