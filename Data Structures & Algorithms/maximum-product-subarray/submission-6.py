class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        mx, mn = 1, 1
        for n in nums:
            tmp = mx * n
            mx = max(mx * n, mn * n, n)
            mn = min(mn * n, tmp, n)
            ans = max(mx, ans)
        return ans 