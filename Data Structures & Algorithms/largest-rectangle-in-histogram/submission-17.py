class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= v:
                startI, val = stack.pop()
                res = max(res, (i - startI) * val)
                start = startI
            stack.append((start,v))
        
        for i,v in stack:
            res = max(res, (len(heights) - i) * v)
        return res