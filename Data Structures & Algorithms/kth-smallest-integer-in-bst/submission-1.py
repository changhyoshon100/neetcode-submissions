# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        unsorted = self.helper(root, arr)
        return sorted(unsorted)[k-1]

    def helper(self, root, arr):
        if not root:
            return
        arr.append(root.val)
        self.helper(root.left, arr)
        self.helper(root.right, arr)
        return arr

        