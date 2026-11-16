class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        val = 1
        maxi = 1
        mini = 1
        for n in nums:
            val = maxi * n 
            maxi = max(n, mini * n, maxi * n)
            mini = min(n, val, mini * n)
            res = max(maxi, mini, res, n)
        return res 
