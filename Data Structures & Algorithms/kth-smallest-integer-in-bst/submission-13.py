class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return None

            left_result = dfs(node.left)
            if left_result is not None:
                return left_result

            count += 1
            if count == k:
                return node.val

            return dfs(node.right)

        return dfs(root)