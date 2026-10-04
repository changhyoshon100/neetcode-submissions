class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first = [0] + nums[1:]
        second = nums[:-1] + [0]
        memo = {}

        def dfs(i, arr):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            rob = dfs(i+2, arr) + arr[i]
            skip = dfs(i+1, arr)
            memo[i] = max(rob, skip)
            
            return memo[i]
        a = dfs(0, first)
        memo = {}
        b = dfs(0, second)
        ans = max(a,b)
        return ans
        
        