class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 == 1: return False
        half = total // 2
        memo = {}
        
        def dfs(i, val):
            if val == half:
                return True
            if val > half or i == len(nums):
                return False
            if (i, val) in memo:
                return memo[(i, val)]
            memo[(i,val)] = dfs(i+1, val + nums[i]) or dfs(i+1, val)
            
            return memo[(i, val)]
        
        return dfs(0, 0)