class SegmentTreeNode:
    def __init__(self, val, L, R):
        self.sum = val
        self.L = L
        self.R = R
        self.left = None
        self.right = None

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTreeNode(nums[L], L, R)
        
        M = (L + R) // 2
        root = SegmentTreeNode(0, L, R)
        root.left = SegmentTreeNode.build(nums, L, M)
        root.right = SegmentTreeNode.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        
        M = (self.L + self.R) // 2
        if index <= M:
            self.left.update(index, val)
        else:
            self.right.update(index, val)
        self.sum = self.left.sum + self.right.sum

    def query(self, L, R):
        if L == self.L and R == self.R:
            return self.sum
        
        M = (self.L + self.R) // 2
        if R <= M:
            return self.left.query(L, R)
        elif L > M:
            return self.right.query(L, R)
        else:
            return self.left.query(L, M) + self.right.query(M+1, R)

class SegmentTree:
    def __init__(self, nums):
        self.root = SegmentTreeNode.build(nums, 0, len(nums) - 1)

    def update(self, idx, val):
        self.root.update(idx, val)

    def query(self, l, r):
        return self.root.query(l, r)

