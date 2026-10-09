class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        val = 0
        
        for R in range(len(nums)):
            if val < 0:
                val = 0
            val += nums[R]
            ans = max(val, ans)
        return ans