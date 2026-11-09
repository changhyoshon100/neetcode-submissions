# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        def dfs(node,i):
            nonlocal res
            if not node:
                return None
            res = max(res, i)
            dfs(node.left, i+1)
            dfs(node.right, i+1)
            return res
        
        return dfs(root,1)
