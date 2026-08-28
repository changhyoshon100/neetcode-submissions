class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                stackIdx, stackVal = stack.pop()
                res = max(res, (i - stackIdx) * stackVal)
                start = stackIdx
            stack.append((start,v))

        for i,v in stack:
            res = max(res, (len(heights) - i) * v)
        return res