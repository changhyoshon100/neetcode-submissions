# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        return self.bfs(root, queue, [], [])
    def bfs(self, root, q, res, level):
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            res.append(level)
            level = []
        return res


