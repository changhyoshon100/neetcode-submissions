class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        res = 0
        while L < R:

            if height[L] <= height[R]:
                L += 1
                res += max((maxL - height[L]), 0)
                maxL = max(maxL, height[L])
            else:
                R -= 1
                res += max((maxR - height[R]), 0)
                maxR = max(maxR, height[R])
        return res
            