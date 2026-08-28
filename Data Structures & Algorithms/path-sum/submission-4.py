# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, targetSum, curr):
            if not node:
                return

            if curr and not node.left and not node.right:
                return targetSum - node.val == sum(curr) 

            curr.append(node.val)
            
            if curr and dfs(node.left, targetSum, curr):
                return True
            if curr and dfs(node.right, targetSum, curr):
                return True

            if curr:
                curr.pop()
            return False
            
        return dfs(root, targetSum, [0])