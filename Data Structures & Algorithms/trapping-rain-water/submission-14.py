class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        res = 0
        l_h = 0
        r_h = 0
        while l < r:
            if height[l] < height[r]:
                l_h = max(height[l], l_h)
                l += 1
                res += max(l_h - height[l], 0)
            else:
                r_h = max(height[r], r_h)
                r -= 1
                res += max(r_h - height[r], 0)
        return res

