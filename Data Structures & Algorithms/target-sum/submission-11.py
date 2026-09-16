class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if i == len(nums) and total == target:
                return 1
            if i == len(nums):
                return 0
            if (i,total) in memo:
                return memo[(i,total)]
            
            a = dfs(i+1, total + nums[i])
            b = dfs(i+1, total - nums[i])
            memo[(i,total)] = a + b
            return memo[(i,total)]
        
        return dfs(0,0)