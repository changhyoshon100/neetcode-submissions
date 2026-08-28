"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None:None}
        ptr = head

        while ptr:
            newNode = Node(ptr.val)
            mp[ptr] = newNode
            ptr = ptr.next
        
        ptr = head
        while ptr:
            mp[ptr].next = mp[ptr.next]
            mp[ptr].random = mp[ptr.random]
            ptr = ptr.next
        return mp[head]