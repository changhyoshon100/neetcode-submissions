# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        first = head
        while list1 and list2:
            print(head.val)
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                head.next = node
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                head.next = node
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1  
        else: head.next = list2
        return first.next