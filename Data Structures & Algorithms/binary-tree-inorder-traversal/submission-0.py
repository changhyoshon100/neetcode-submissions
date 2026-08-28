# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return []
        return self.bucket(ans, root)
        
    
    def bucket(self, ans, tree):
        if not tree:
            return 
        self.bucket(ans, tree.left)
        ans.append(tree.val)
        self.bucket(ans, tree.right)
        return ans
        



