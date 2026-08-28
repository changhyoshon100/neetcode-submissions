class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = len(nums)
        total = 0
        ans = len(nums)
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = R - L + 1
                total -= nums[L]
                L += 1
            ans = min(ans, length)
        
        if sum(nums) < target: return 0
        if ans == len(nums): return len(nums)
        return ans 

            
            
        