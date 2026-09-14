class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = 1,1
        ans = max(nums)
        for n in nums:
            tmp = mx * n
            mx = max(mx * n, n, mn * n)
            mn = min(tmp, n, mn * n)
            ans = max(mx, mn, n, ans)
            
        return ans