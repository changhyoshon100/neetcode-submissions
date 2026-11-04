class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_ht = height[left]
        r_ht = height[right]
        res = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                l_ht = max(l_ht, height[left])
                res += (l_ht - height[left])
            else:
                right -= 1
                r_ht = max(r_ht, height[right])
                res += (r_ht - height[right])
        return res
            