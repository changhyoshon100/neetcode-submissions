class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        area = 0
        maxArea = 0
        R = len(heights) - 1
        while L < R:
            width = (R - L)
            ht = min(heights[L], heights[R])
            area = width * ht
            maxArea = max(area, maxArea)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            
        return maxArea
            

            