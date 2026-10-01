class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = 1,1
        res = float('-inf')
        for n in nums:
            temp = mx * n
            mx = max(mx * n, mn * n, n)
            mn = min(temp, mn * n, n)
            res = max(mx, mn, res)
        return res
