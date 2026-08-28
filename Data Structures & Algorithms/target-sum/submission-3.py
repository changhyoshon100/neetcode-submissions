class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, t):
            if i == len(nums) and t == 0:
                return 1
            if i == len(nums):
                return 0
            # add
            res = (dfs(i+1, t - nums[i]) + 
            # subtract
            dfs(i+1, t + nums[i]))
            return res
        return dfs(0,target)
