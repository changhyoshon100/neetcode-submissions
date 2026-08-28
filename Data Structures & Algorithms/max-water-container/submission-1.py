class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        area = 0
        res = 0
        while L < R:
            width = R - L
            height = min(heights[L], heights[R])
            area = width * height 
            res = max(area, res)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return res
            

        
            