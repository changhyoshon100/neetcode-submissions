# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        char1 = ""
        char2 = ""
        stack1 = []
        stack2 = []
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1 = l1.next
            if l2: 
                stack2.append(l2.val)
                l2 = l2.next
        # print(stack1, stack2)
        while stack1 or stack2:
            if stack1:
                char1 += str(stack1.pop())
            if stack2:
                char2 += str(stack2.pop())
        
        char1 = int(char1)
        char2 = int(char2)
        added = str(char1 + char2)
        length = len(added)
        node = ListNode()
        ptr = node
        for i in range(length - 1, -1, -1):
            # print(i, added)
            val = int(added[i])
            # print(val)
            node.next = ListNode(val)
            node = node.next
        return ptr.next
        
        