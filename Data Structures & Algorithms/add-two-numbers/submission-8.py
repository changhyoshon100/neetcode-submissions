# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            digit = l1.val + l2.val 
            remainder = digit % 10 + carry
            carry = digit // 10
            newNode = ListNode(remainder)
            curr.next = newNode
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        

        while l1 and curr:
            curr.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            curr = curr.next
            l1 = l1.next
        while l2 and curr:
            curr.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            curr = curr.next
            l2 = l2.next
        if not l1 and not l2 and carry == 1:
            curr.next = ListNode(carry)
            curr = curr.next
            return dummy.next
        return dummy.next
            