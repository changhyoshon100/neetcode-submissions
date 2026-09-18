# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            nonlocal diameter

            if not node:
                return 0

            diameter = max(diameter, depth(node.left) + depth(node.right))
            return 1 + max(depth(node.left), depth(node.right))

        depth(root)
        return diameter