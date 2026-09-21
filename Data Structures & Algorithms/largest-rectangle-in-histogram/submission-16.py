class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= v:
                stackIdx, stackVal = stack.pop()
                res = max(res, (i - stackIdx) * stackVal)
                start = stackIdx
            stack.append((start,v))
        
        for i,v in stack:
            res = max((len(heights) - i) * v, res)
        
        return res