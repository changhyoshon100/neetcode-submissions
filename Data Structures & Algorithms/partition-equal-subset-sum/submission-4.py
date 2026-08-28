class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = set()
        if total % 2 != 0:
            return False
        def dfs(curr, i):
            if i >= len(nums):
                return False
            if curr == total // 2:
                return True
            if (curr, i) in memo:
                return False

            if dfs(curr, i+1):
                return True
            if dfs(curr + nums[i], i+1):
                return True
            
            memo.add((curr,i))
            return False
            
        return dfs(0, 0)