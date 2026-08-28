class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        memo2 = {}
        def dfs0(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs0(i+2) + nums[i], dfs0(i+1))
            return memo[i]

        def dfs1(i):
            if i >= len(nums):
                return 0
            if i in memo2:
                return memo2[i]
            
            memo2[i] = max(dfs1(i+2) + nums[i], dfs1(i+1))
            return memo2[i]

        
        return max(dfs0(0), dfs1(1))