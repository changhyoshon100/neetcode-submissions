class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)

        half = total / 2
        if half != total // 2:
            return False
        
        def dfs(i,total):
            if i == len(nums):
                return False
            if total == half:
                return True
            if (i,total) in memo:
                return memo[(i,total)]
            a = dfs(i+1, total + nums[i])
            b = dfs(i+1, total)
            memo[(i,total)] = a or b
            return memo[(i,total)]

        
        return dfs(0,0)
        
