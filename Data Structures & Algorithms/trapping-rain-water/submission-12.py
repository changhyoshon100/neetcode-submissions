class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        area = 0
        maxL, maxR = 0,0
        while L < R:
            if height[L] < height[R]:
                maxL = max(maxL, height[L])
                L += 1
                if maxL - height[L] > 0:
                    area += (maxL - height[L])
            else:
                maxR = max(maxR, height[R])
                R -= 1
                if maxR - height[R] > 0:
                    area += (maxR - height[R])
        return area
            
