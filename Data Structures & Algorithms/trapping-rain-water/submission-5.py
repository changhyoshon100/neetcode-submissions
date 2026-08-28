class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        leftMax, rightMax = 0,0
        res = 0
        while L < R:
            if height[L] < height[R]:
                leftMax = max(leftMax, height[L])
                res += (leftMax - height[L])
                L += 1
            else:
                rightMax = max(rightMax, height[R])
                res += (rightMax - height[R])
                R -= 1
        return res
