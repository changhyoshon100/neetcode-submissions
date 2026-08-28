# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def dfs(node, cnt):
            if not node:
                return None
            
            mp[cnt].append(node.val)
            dfs(node.left, cnt + 1)
            dfs(node.right, cnt + 1)
            return mp
        
        dfs(root,0)
        return list(mp.values())