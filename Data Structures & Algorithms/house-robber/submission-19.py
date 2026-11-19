class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            res = 0
            res = max(dfs(i+1), dfs(i+2) + nums[i])
            memo[(i)] = res
            return res
        
        return dfs(0)