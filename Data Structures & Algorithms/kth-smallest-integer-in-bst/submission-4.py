# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        
        def dfs(node):
            if not node:
                return
            minHeap.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        # print(minHeap)
        # minHeap = [-s for s in minHeap]
        heapq.heapify(minHeap)
        while k > 1:
            heapq.heappop(minHeap)
            k -= 1
        return minHeap[0]