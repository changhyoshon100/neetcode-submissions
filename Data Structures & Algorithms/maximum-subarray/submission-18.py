class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        res = min(nums)
        for R in range(len(nums)):
            if ans < 0:
                ans = 0
            ans += nums[R]
            res = max(res, ans)
        return res
            
            
