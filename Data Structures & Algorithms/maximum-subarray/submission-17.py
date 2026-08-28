class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        L = 0
        ans = float('-inf')
        for R in range(len(nums)):
            # print(total, ans)
            total += nums[R]
            if total < 0:
                L = R
                total = 0
            else:
                ans = max(ans, total)

            
        
        return ans if ans != float('-inf') else max(nums)