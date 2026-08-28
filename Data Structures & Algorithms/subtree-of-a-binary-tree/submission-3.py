# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subdfs(rt,srt):
            if not rt and not srt:
                return True
            if (not rt or not srt) or (rt.val != srt.val):
                return False
            return subdfs(rt.left, srt.left) and subdfs(rt.right, srt.right)

        def dfs(rt, srt):
            if not rt:
                return False
            if not srt:
                return True

            if subdfs(rt,srt):     
                return True

            return dfs(rt.left, subRoot) or dfs(rt.right, subRoot)
        return dfs(root, subRoot)