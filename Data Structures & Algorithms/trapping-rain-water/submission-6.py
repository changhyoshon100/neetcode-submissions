class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        area = 0
        R = len(height) - 1
        maxHt_l = 0
        maxHt_r = 0
        while L < R:
            
            if height[L] < height[R]:
                maxHt_l = max(maxHt_l, height[L])
                L += 1
                area += max((maxHt_l - height[L]),0)
                
            else:
                maxHt_r = max(maxHt_r, height[R])
                R -= 1
                area += max((maxHt_r - height[R]),0)
        return area


