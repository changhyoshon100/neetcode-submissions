# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)

        def dfs(node,i):
            if not node:
                return None
            
            if i not in mp:
                mp[i] = node.val
            dfs(node.right,i+1)
            dfs(node.left,i+1)
        
        dfs(root,0)

        return list(mp.values())

        