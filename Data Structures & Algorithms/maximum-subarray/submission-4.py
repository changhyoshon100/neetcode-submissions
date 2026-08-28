class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
        return maxSum

            
                
