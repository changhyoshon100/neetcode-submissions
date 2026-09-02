# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, large):
            if not node:
                return 0
            cnt = 0
            
            if node.val >= large:
                cnt = 1
            
            large = max(large, node.val)

            return dfs(node.left, large) + dfs(node.right, large) + cnt
        
        return dfs(root, root.val)