class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal, minVal = 1,1
        ans = max(nums)
        for n in nums:
            tmp = maxVal * n
            maxVal = max(minVal * n, maxVal * n, n)
            minVal = min(tmp, minVal * n, n)
            ans = max(maxVal, ans)
        return ans

