class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        for i in range(n):
            curSum = 0
            for j in range(i, i + n):
                curSum += nums[j % n]
                maxSum = max(maxSum, curSum)
                if curSum < 0:
                    curSum = 0
        return maxSum
                
