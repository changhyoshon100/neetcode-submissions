class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True 

            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            height = 1 + max(left_height, right_height)
            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            return height, balanced

        _, is_balanced = dfs(root)
        return is_balanced