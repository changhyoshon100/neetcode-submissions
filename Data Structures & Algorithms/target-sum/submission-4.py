class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, t):
            if i == len(nums) and t == 0:
                return 1
            if i == len(nums):
                return 0
            if (i,t) in memo:
                return memo[(i,t)]
            # add
            memo[(i,t)] = (dfs(i+1, t - nums[i]) + 
            # subtract
            dfs(i+1, t + nums[i]))
            return memo[(i,t)]
        return dfs(0,target)
