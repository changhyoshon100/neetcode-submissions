# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        carry = 0 
        ptr = node
        while l1 and l2:
            added = l1.val + l2.val
            remain = added % 10
            node.next = ListNode(remain + carry)
            node = node.next
            carry = added // 10
            l1 = l1.next
            l2 = l2.next
        
        added = 0
        while l1 or l2:
            if l1:
                added = carry + l1.val
                node.next = ListNode(added % 10)
                l1 = l1.next
            elif l2:
                added = carry + l2.val
                node.next = ListNode(added % 10)
                l2 = l2.next
            node = node.next
            carry = added // 10
        if carry:
            node.next = ListNode(carry)
        return ptr.next



        