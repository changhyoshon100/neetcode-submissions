class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = 0
        def dfs(i, curr):
            if i == N:
                return curr == target

            return dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
        return dfs(0,0)