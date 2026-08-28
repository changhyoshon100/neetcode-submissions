class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = 1,1
        ans = max(nums)
        for n in nums:
            tmp = mx * n
            mx = max(mx * n, mn * n, n)
            mn = min(mn * n, tmp, n)
            
            ans = max(ans, mx)
        return ans