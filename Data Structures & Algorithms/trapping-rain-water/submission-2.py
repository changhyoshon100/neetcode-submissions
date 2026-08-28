class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        res = 0
        while L < R:
            # print(L,R, res)
            if height[L] < height[R]:
                if leftMax <= height[L]:
                    leftMax = height[L]
                    L += 1
                else:
                    res += (leftMax - height[L])
                    L += 1
            else:
                if rightMax <= height[R]:
                    rightMax = height[R]
                    R -= 1
                else:
                    res += (rightMax - height[R])
                    R -= 1
        return res

            