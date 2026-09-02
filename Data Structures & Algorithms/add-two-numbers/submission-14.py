# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        total = int(num1) + int(num2)
        
        dummy = ListNode(0)
        if total == 0: return dummy
        ptr = dummy
        while total > 0:
            val = total % 10
            total = total // 10
            
            node = ListNode(val)
            dummy.next = node
            dummy = dummy.next
        return ptr.next

