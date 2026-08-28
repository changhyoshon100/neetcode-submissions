# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.remove(root, key)
    
    def findSmallest(self, root, key):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def remove(self, root, key):
        if not root:
            return root
        
        if root.val < key:
            root.right = self.remove(root.right,key)
        elif root.val > key:
            root.left = self.remove(root.left, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                node = self.findSmallest(root.right, key)
                root.val = node.val
                root.right = self.remove(root.right, root.val)
        return root




