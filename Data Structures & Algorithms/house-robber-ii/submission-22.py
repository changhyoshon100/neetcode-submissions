class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        f_nums = nums[1:]
        l_nums = nums[:-1]
        res = 0
        
        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i+2, nums, memo) + nums[i], dfs(i+1, nums, memo))
            return memo[i]
        ans = max(dfs(0, f_nums, {}), dfs(1,f_nums, {}))
        ans2 = max(dfs(0, l_nums, {}), dfs(1,l_nums, {}))
        return max(ans, ans2)
            
        
