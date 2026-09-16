class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}
        if total % 2 != 0:
            return False
        ans = total // 2
        def dfs(i, total):
            if total == ans:
                return True
            if total < ans:
                return False
            if i == len(nums):
                return False
            if (i, total) in memo:
                return memo[(i,total)]

            
            a = dfs(i+1, total - nums[i])
            b = dfs(i+1, total)
            memo[(i,total)] = a or b
            return memo[(i,total)]

        return dfs(0, total)
