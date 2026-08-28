class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        ans = 0
        def dfs(i, total):
            nonlocal ans
            if i == len(nums) and total == target:
                return 1
            if i == len(nums) and total != target:
                return 0
            if (i, total) in memo:
                return memo[(i,total)]
            
            ans = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
            memo[(i,total)] = ans

            return memo[(i,total)]
        
        return dfs(0,0)