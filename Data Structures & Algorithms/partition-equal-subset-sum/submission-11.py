class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total %2 != 0:
            return False
        half = total // 2
        
        def dfs(i,val):
            if i == len(nums):
                return False
            if val == half:
                return True
            if (i,val) in memo:
                return memo[(i,val)]
            
            use = dfs(i+1,val + nums[i])
            skip = dfs(i+1,val)
            memo[(i,val)] = use or skip
            return memo[(i,val)]
        
        return dfs(0,0)