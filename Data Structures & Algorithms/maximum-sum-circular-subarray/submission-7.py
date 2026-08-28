class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        globMax = nums[0]
        globMin = nums[0]

        total = 0
        for n in nums:
            curMax = max(n, curMax + n)
            globMax = max(curMax, globMax)
            total += n
            curMin = min(n, curMin + n)
            globMin = min(curMin, globMin)
        return max(globMax, total - globMin) if globMax > 0 else globMax