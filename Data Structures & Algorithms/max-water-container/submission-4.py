class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0, len(heights) - 1
        width = 0
        ht = 0
        area = 0
        while L < R:
            ht = min(heights[L], heights[R])
            width = R - L 
            area = max(area,ht * width)

            if heights[L] < heights[R]:
                L +=1
            else:
                R -= 1
            
        return area
            
