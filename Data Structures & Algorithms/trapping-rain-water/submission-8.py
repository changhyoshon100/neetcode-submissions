class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L, R = 0, len(height) - 1
        area = 0
        leftMax = 0
        rightMax = 0
        while L < R:
            if height[L] < height[R]:
                leftMax = max(leftMax, height[L])
                L += 1
                area += max(leftMax - height[L], 0)
            else:
                rightMax = max(rightMax, height[R])
                R -= 1
                area += max(rightMax - height[R], 0)
        return area

