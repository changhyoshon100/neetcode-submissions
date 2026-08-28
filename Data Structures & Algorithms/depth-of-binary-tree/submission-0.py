# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(depth, node):
            if not node:
                return depth
            depth = max(helper(depth+1, node.left),helper(depth+1,node.right))
            return depth
        res = helper(0, root)
        return res