# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.itr = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:
        self.itr += 1
        print(self.arr[self.itr-1])
        return self.arr[self.itr-1]
        
    def hasNext(self) -> bool:
        if self.itr-1 == len(self.arr)-1: return False
        else: return True
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()