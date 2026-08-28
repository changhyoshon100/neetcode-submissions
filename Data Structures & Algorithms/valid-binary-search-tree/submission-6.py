# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(low, high, prev):
            if not prev:
                return True

            if not (low < prev.val and high > prev.val):
                return False
            


            return dfs(prev.val, high, prev.right) and dfs(low, prev.val, prev.left)
        
        return dfs(float('-inf'), float('inf'), root)