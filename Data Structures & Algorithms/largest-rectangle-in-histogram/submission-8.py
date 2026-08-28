class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        for i,v in enumerate(heights):
            start = i
            while stack and stack[-1][1] > v:
                stackIdx, stackVal = stack.pop()
                maxArea = max(maxArea, (i - stackIdx) * stackVal)
                start = stackIdx
            stack.append((start,v))
        
        for i,v in stack:
            maxArea = max(maxArea, (len(heights) - i) * v)
        return maxArea