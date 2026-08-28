"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = defaultdict(list)

        path = set()
        
        def dfs(node):
            if not node:
                return None
            if node in mp:
                return mp[node]

            newNode = Node(node.val)
            mp[node] = newNode

            for nei in node.neighbors:
                # if nei in path:
                #     continue
                newNode.neighbors.append(dfs(nei))
            return newNode

        return dfs(node)
                

        