# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        def dfs(node, arr):
            if not node:
                return 
            
            dfs(node.next, arr)
            arr.append(node.val)
        dfs(head,arr)
        ptr = ListNode(-1)
        rev = ptr
        for a in arr:
            ptr.next = ListNode(a)
            ptr = ptr.next
        return rev.next
