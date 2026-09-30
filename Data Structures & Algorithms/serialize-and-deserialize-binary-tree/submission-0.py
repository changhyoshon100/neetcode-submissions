# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        tokens = []

        def dfs(node):
            if node is None:
                tokens.append("#")
                return

            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data):
        tokens = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            token = tokens[index]
            index += 1

            if token == "#":
                return None

            node = TreeNode(int(token))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
