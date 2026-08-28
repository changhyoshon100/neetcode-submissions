class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackIdx, stackVal = stack.pop()
                maxArea = max(maxArea, stackVal * (i - stackIdx))
                start = stackIdx
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(h * (len(heights) - i), maxArea)
        return maxArea