class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        res = 0
        def dfs(attempt, i, arr):
            if attempt == 'first':
                arr[0] = 0
                attempt = 'done'

            if attempt == 'second': 
                arr[-1] = 0
                attempt = 'done'

            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            a = dfs(attempt, i+2, arr) + arr[i]
            b = dfs(attempt, i+1, arr)
            memo[i] = max(a,b)
            return memo[i]
        
        arr = nums.copy()
        res = max(res, dfs("first", 0, nums))
        memo = {}
        
        # print(res, arr)
        res = max(res, dfs("second", 0, arr))
        return res
        





