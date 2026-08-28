# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(node, prev):
            if not node:
                return 0
            nonlocal cnt

            if node.val >= prev:
                cnt = 1 
            else: cnt = 0
            prev = max(node.val, prev)
            cnt = cnt + dfs(node.left, prev) + dfs(node.right, prev)
            return cnt

        
        return dfs(root, float('-inf'))