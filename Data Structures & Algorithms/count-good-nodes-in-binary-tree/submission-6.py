# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev, ans):
            if not node:
                return 0
            
            if node.val >= prev:
                ans = 1
            else: ans = 0
            prev = max(node.val, prev)
            return ans + dfs(node.left, prev, ans) + dfs(node.right, prev, ans)
        
        return dfs(root, root.val, 0)