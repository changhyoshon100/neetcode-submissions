class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2
        memo = {}

        def dfs(i, target):
            if target == half:
                return True
            if i == len(nums) or target > half:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            # use
            use = dfs(i + 1, target + nums[i])

            # skip
            skip = dfs(i + 1, target)

            memo[(i,target)] = use or skip
            return memo[(i,target)]
        
        return dfs(0,0)
            