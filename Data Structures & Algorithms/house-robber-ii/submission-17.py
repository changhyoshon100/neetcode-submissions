class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] 
        f_nums = nums[1:]
        l_nums = nums[:-1]
        
        def roundRob(arr):
            memo = {}
            def dfs(i,arr):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i] + dfs(i+2,arr), dfs(i+1,arr))
                return memo[i]
            return dfs(0,arr)
        return max(roundRob(f_nums), roundRob(l_nums))