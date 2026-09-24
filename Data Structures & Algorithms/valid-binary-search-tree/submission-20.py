# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, large, small):
            if not node:
                return True
            
            if node.val >= large: return False
            if node.val <= small: return False

            return dfs(node.left, node.val, small) and dfs(node.right, large, node.val)

        
        return dfs(root, float('inf'), float('-inf'))