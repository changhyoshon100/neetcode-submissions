class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = 0
        memo = {} 
        def dfs(i, curr):
            if i == N:
                if curr == target:
                    memo[(i, curr)] = 1
                return curr == target
            if (i, curr) in memo:
                return memo[(i, curr)]
            return dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
        return dfs(0,0)