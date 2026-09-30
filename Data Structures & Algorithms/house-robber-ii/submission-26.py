class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i,total,nums):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i + 2, total,nums) + nums[i], dfs(i + 1, total,nums))
            return memo[i]
        res = 0
        temp = nums.copy()
        for i in range(2):
            memo = {}
            if i == 0:
                arr = temp[:-1]
            else:
                arr = temp[1:]
            res = max(res, dfs(0,0,arr))
        
        return res