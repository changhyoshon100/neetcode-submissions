# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, par):
            nonlocal res
            if not node:
                return 0
            
            if node.val >= par.val:
                res += 1
                dfs(node.left, node)
                dfs(node.right, node)
            else:
                dfs(node.left, par)
                dfs(node.right, par)

        dfs(root, root)
        return res