# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,target,ans):
            if not node:
                return 0
            
            if node.val >= target:
                ans = 1
            else: ans = 0

            target = max(target, node.val)

            return ans + dfs(node.left,target,ans) + dfs(node.right,target,ans)
            
        return dfs(root,root.val,0)
        