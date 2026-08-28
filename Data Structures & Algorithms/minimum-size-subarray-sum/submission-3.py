class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        N = len(nums)
        res = 0
        length = float('inf')
        
        for R in range(N):
            res += nums[R]
            while res >= target:
                res -= nums[L]
                length = min(R - L + 1, length)
                L += 1
        return 0 if length == float('inf') else length
            