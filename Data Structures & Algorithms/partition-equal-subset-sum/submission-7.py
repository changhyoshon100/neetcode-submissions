class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
            
        memo = {}
        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            
            # include 
            inc = dfs(i+1, target - nums[i])
            # not include
            skip = dfs(i+1, target)
            memo[(i, target)] = (inc or skip)
            return memo[(i, target)]
        
        return dfs(0, target)