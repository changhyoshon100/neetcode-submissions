class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dfs_f(i, memo):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs_f(i+2, memo) + nums[i], dfs_f(i+1, memo))
            return memo[i]

        def dfs_s(i, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs_s(i+2, memo) + nums[i], dfs_s(i+1, memo))
            return memo[i]
        res = 0
        
        memo1 = {}
        a = dfs_f(0, memo1)
        memo2 = {}
        b = dfs_s(1, memo2)
        return max(a,b)
        
        
        