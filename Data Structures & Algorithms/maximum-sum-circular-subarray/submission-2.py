class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin, currMax = 0,0
        globMin, globMax = nums[0], nums[0]
        total = 0
        for num in nums:
            currMax = max(num, currMax + num)
            currMin = min(num, currMin + num)
            total += num
            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)
        
        return max(globMax, total - globMin) if globMax > 0 else globMax

