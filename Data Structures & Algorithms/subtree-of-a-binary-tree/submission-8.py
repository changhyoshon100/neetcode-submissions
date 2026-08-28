# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(n1, n2):
            if  not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            
            return same(n1.left, n2.left) and same(n1.right, n2.right)
        res = False
        def dfs(root):
            nonlocal res
            if not root:
                return True
            dfs(root.left)
            dfs(root.right)
            res = res or same(root, subRoot)
            return res
        return dfs(root)
            
            




