class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
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
            
            return dfs(i+1, total - nums[i]) or dfs(i+1, total)

        return dfs(0, total)
