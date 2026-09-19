# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS -> Save by level
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = [[root.val]]

        def bfs():
            nonlocal queue
            while queue:
                next_q = deque()
                
                for node in queue:
                    if node.left:
                        next_q.append(node.left)
                    if node.right:
                        next_q.append(node.right)
                
                if next_q:
                    result.append([node.val for node in next_q])
                queue = next_q

        bfs()
        return result