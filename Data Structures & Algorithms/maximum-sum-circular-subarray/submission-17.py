class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0: return max(nums)
        total = sum(nums)
        curMin = 0
        allMin = 0
        for i in range(len(nums)):
            curMin = min(curMin + nums[i], 0)
            allMin = min(curMin, allMin)
        curMax = 0
        allMax = 0
        for i in range(len(nums)):
            curMax = max(curMax + nums[i], 0)
            allMax = max(curMax, allMax)


        return total - allMin if allMax < total - allMin else allMax
            