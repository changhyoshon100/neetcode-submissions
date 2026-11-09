# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        
        prev, curr = None, first
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        node1, node2 = head, prev

        while node1.next and node2.next:
            temp1, temp2 = node1.next, node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2
        

        






