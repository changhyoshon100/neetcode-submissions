class Solution:
    def trap(self, height: List[int]) -> int:
        maxL, left = height[0],0
        maxR, right = height[len(height) - 1], len(height) - 1
        total = 0
        while left < right:
    
            if height[left] < height[right]:
                h_l = max(maxL - height[left],0)
                total += h_l
                left += 1
                maxL = max(maxL, height[left])
            else:
                h_r = max(maxR - height[right], 0)
                total += h_r
                right -= 1
                maxR = max(maxR, height[right])
            
        return total

            



            