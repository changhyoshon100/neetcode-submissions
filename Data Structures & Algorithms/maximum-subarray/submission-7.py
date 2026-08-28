class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L,R = 0,0
        curSum = 0
        maxSum = -10**9
        for R in range(len(nums)):
            curSum = curSum + nums[R]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                L = R
                curSum = 0
            
            
        return maxSum

                
                