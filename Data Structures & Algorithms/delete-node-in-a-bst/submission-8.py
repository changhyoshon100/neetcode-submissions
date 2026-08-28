# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return
            
            if node.val < key:
                node.right = dfs(node.right, key)
            elif node.val > key:
                node.left = dfs(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    cur = node.right 
                    while cur.left:
                        cur = cur.left
                    node.val = cur.val
                    node.right = dfs(node.right, node.val)
            return node

        
        return dfs(root, key)