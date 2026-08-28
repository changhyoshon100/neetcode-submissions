class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        globMax = -10**9
        
        for i in range(n):
            curMax = -10**9
            for j in range(i,i + n):
                curMax = max(curMax + nums[j % n], nums[j % n])
                globMax = max(globMax, curMax)
        return globMax
