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
            return dfs(arr, i)
        
        arr1 = nums[1:]
        arr2 = nums[:-1]

        return max(robline(arr1, 0), robline(arr2, 0))