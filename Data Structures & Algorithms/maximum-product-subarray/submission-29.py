class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = 1,1 
        res = float('-inf')

        for n in nums:
            tmp = mx * n
            mx = max(mx * n, mn * n, n)
            mn = min(mn * n, tmp, n)
            res = max(res, mx, mn, n)
        return res