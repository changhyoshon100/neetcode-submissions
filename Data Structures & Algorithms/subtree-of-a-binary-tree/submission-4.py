# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subdfs(root, sroot):
            if not root and not sroot:
                return True
            if not root or not sroot:
                return False
            if root.val != sroot.val:
                return False
            
            return subdfs(root.left, sroot.left) and subdfs(root.right, sroot.right)
        
        def dfs(root):
            if not root:
                return False
            if subdfs(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
            
        
