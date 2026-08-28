class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # for not circular
        curMax = 0
        maxSum = 0

        # for circular
        curMin = 0
        minSum = 0
        
        total = 0

        for i in range(len(nums)):
            curMax += nums[i]
            curMax = max(curMax, 0)
            maxSum = max(maxSum, curMax)

            curMin = min(curMin+nums[i], nums[i])
            minSum = min(minSum, curMin)
            total += nums[i]
        if max(nums) < 0: return max(nums)
        return max(total - minSum, maxSum) 


            


