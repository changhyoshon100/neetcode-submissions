# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            root.left.val += root.val * 10 
            root.right.val += root.val * 10 
            return self.sumNumbers(root.left) + self.sumNumbers(root.right)
        elif root.left:
            root.left.val += root.val * 10 
            return self.sumNumbers(root.left)
        elif root.right:
            root.right.val += root.val * 10 
            return self.sumNumbers(root.right)
        else:
            return root.val