# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoList(lists[i-1], lists[i])
        return lists[-1]
        
    def mergeTwoList(self,l1, l2):
        cur = ListNode()
        ptr = cur
        addVal = 0
        while l1 and l2:
            if l1.val < l2.val:
                addVal = l1.val
                l1 = l1.next
            else:
                addVal = l2.val
                l2 = l2.next
            addNode = ListNode(addVal)
            cur.next = addNode
            cur = cur.next
        
        while l1:
            
            cur.next = ListNode(l1.val)
            l1 = l1.next
            cur = cur.next
            
        while l2:
            
            cur.next = ListNode(l2.val)
            l2 = l2.next
            cur = cur.next
        

        return ptr.next
