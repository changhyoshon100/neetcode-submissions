# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx, val in enumerate(inorder)}
        self.idx = 0

        def dfs(l, r):
            if l > r:
                return None
            # same as value in indices
            root_val = preorder[self.idx]
            self.idx += 1
            # create node with the inorder value
            root = TreeNode(root_val)
            # index of value in indices
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(preorder) - 1)
