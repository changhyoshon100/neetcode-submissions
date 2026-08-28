class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0: return max(nums)
        curSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            curSum = max(curSum + nums[i], 0)
            maxSum = max(maxSum, curSum)
        return maxSum
            