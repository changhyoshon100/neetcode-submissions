class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def robline(arr, i):
            memo = {}
            def dfs(arr, i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(arr[i] + dfs(arr, i+2), dfs(arr, i+1))
                return memo[i]
            return dfs(arr,i)
        first = nums[1:]
        second = nums[:-1]
        return max(robline(first,0), robline(second,0))