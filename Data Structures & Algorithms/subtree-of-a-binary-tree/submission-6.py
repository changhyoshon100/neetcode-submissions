# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameT(n1, n2):
            if not n1 and not n2: return True
            if (not n1 or not n2): return False 
            if (n1.val != n2.val): return False 
    
            return sameT(n1.left, n2.left) and sameT(n1.right, n2.right) 

        
        def dfs(root):
            if not root:
                return False
            if sameT(root, subRoot): return True 
            
            return (dfs(root.left) or dfs(root.right))
        return dfs(root)