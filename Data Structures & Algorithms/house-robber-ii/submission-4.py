class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robline(i, nums):
            memo = {}
            def dfs(i, nums):
                if i >= len(nums):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(nums[i] + dfs(i+2, nums), dfs(i+1,nums))
                return memo[i]
            return dfs(i,nums)

        nums_rmfst = nums[1:]
        nums_rmlst = nums[:-1]

        return max(robline(0,nums_rmfst), robline(0,nums_rmlst))
