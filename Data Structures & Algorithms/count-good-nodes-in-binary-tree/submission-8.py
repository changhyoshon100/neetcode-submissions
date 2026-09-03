# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, grand):
            if not node:
                return 0
            cnt = 0
            if node.val >= grand:
                cnt = 1
            grand = max(node.val, grand)
            
            return dfs(node.left, grand) + dfs(node.right, grand) + cnt

        return dfs(root, root.val)