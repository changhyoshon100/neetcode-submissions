class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dfs(i, arr, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            
            res = max(dfs(i+1, arr, memo), dfs(i+2, arr, memo) + arr[i]) 
            memo[i] = res
            return res

        first = nums[1:]
        second = nums[:-1]
        
        a = dfs(0, first, {})
        b = dfs(0, second, {})
        
        return max(a,b)

        