class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        ans = max(nums)
        for n in nums:
            res += n 
            if res < 0:
                res = 0
            ans = max(res, ans)
            
        return ans if ans != 0 else max(nums)