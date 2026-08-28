# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        mp = defaultdict(int)
        def dfs(node, res, lv):
            if not node:
                return None
            if lv not in mp:
                res.append(node.val)
            mp[lv] = node.val
            lv += 1
            dfs(node.right, res, lv)
            dfs(node.left, res, lv)
            return res
        
        return dfs(root, [], 0)
        
