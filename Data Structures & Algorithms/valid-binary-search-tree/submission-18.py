# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, par_l, par_r):
            if not node:
                return True
            
            if par_l <= node.val:
                return False
            if par_r >= node.val:
                return False

            return dfs(node.left, node.val, par_r) and dfs(node.right, par_l, node.val)

        
        return dfs(root, float('inf'), float('-inf'))