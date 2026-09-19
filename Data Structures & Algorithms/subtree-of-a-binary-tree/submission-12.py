# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS -> root.val == subRoot.val then 
# use recursion to see is the same tree or not
# 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        def isSame(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and t2 and t1.val == t2.val:
                return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
            else:
                return False

        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
