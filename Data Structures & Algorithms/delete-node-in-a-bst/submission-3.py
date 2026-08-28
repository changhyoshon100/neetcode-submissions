# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.search(root, key)
        
    def findSmallest(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def search(self, root, key):
        if not root:
            return root
        
        if root.val > key:
            print(root.val)
            root.left = self.search(root.left, key)
        elif root.val < key:
            print(root.val)
            root.right = self.search(root.right, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                node = self.findSmallest(root.right)
                root.val = node.val
                root.right = self.search(root.right, node.val)
        return root










