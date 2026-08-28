# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        level = []
        res.append(root.val)
        queue = deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr and curr.right:
                    queue.append(curr.right)
                if curr and curr.left:
                    queue.append(curr.left)

                if curr and curr.right and not level:
                    level.append(curr.right.val)
                if curr and not curr.right and curr.left and not level:
                    level.append(curr.left.val)
            if level:
                res.append(level[0])
            level = []

        return res

            
        