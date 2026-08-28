# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, prev, cnt):
            nonlocal res
            if not node:
                return 0
            if prev.val <= node.val:
                cnt = 1
            else: cnt = 0
                
            prev = TreeNode(max(node.val, prev.val))
            return cnt + dfs(node.left, prev, cnt) + dfs(node.right, prev, cnt)

        
        return dfs(root, root, 0)