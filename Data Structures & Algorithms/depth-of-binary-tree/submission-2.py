# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, res):    
            if not node:
                return res
            return max(dfs(node.left, res+1), dfs(node.right, res+1))

        return dfs(root, 0)