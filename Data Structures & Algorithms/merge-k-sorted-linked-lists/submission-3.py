# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def arrange(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    addVal = l1.val
                    l1 = l1.next 
                else:
                    addVal = l2.val
                    l2 = l2.next 
                addNode = ListNode(addVal)
                curr.next = addNode
                curr = curr.next

            while l1:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next

            while l2:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next

            return dummy.next
        if not lists: return None
        
        for i in range(1, len(lists)):
            lists[i] = arrange(lists[i-1], lists[i])
        return lists[-1]

                
                
                