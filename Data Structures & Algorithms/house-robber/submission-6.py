class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,res):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            res = max(nums[i] + dfs(i+2,res), dfs(i+1,res))
            memo[i] = res
            return res
        
        return dfs(0,0)
