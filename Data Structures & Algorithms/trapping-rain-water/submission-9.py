class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        L, R = 0, len(height) - 1
        leftMax, rightMax = 0,0
        while L < R:
            
            if height[L] < height[R]:
                leftMax = max(height[L], leftMax)
                L += 1
                area += max(leftMax - height[L],0)
            else:
                rightMax = max(height[R], rightMax)
                R -= 1
                area += max(rightMax - height[R],0)
        return area

                
                