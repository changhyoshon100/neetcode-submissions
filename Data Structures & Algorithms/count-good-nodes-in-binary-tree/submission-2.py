# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev, cnt):
            if not node:
                return 0
            if prev <= node.val:
                cnt = 1
            else: cnt = 0
                
            prev = max(node.val, prev)
            return cnt + dfs(node.left, prev, cnt) + dfs(node.right, prev, cnt)

        
        return dfs(root, root.val, 0)