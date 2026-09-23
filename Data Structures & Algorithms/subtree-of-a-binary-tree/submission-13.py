# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            
            if node.val != sub.val:
                return False

            return sameTree(node.left, sub.left) and sameTree(node.right, sub.right)
        flag = True
        def dfs(node):
            if not node:
                return False
        
            flag = sameTree(node, subRoot)
                
            a = dfs(node.left)
            b = dfs(node.right)
            
            return a or b or flag

        ans = False
        ans = ans or dfs(root)
        
        return ans
        
