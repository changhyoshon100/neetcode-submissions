# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, checkVal):
            if not node:
                return 0
            add = 0
            if checkVal <= node.val:
                add = 1
                checkVal = max(checkVal, node.val)

            left = dfs(node.left, checkVal)
            right = dfs(node.right, checkVal)

            return left + right + add
        
        return dfs(root,float('-inf'))