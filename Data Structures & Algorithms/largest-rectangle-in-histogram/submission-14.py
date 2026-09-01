class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                stackIdx, stackVal = stack.pop()
                maxArea = max((i - stackIdx) * stackVal, maxArea)
                start = stackIdx
            stack.append((start,v))

        for i,v in stack:
            maxArea = max(maxArea, (len(heights) - i) * v)
        return maxArea