class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if half != total / 2:
            return False
        memo = {}
        def dfs(i,val):
            if val > half:
                return False
            if i == len(nums):
                return False
            if val == half:
                return True
            if (i,val) in memo:
                return memo[(i,val)]
            
            a = dfs(i+1, val + nums[i])
            b = dfs(i+1, val)
            memo[(i,val)] = a or b
            return memo[(i,val)]
        
        return dfs(0,0)
        