class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        f_nums = nums[1:]
        s_nums = nums[:-1]
        def roundRob(nums):
            memo = {}
            def dfs(arr,i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i] + dfs(arr,i+2), dfs(arr,i+1))
                return memo[i]

            return dfs(nums, 0)
        return max(roundRob(f_nums), roundRob(s_nums))