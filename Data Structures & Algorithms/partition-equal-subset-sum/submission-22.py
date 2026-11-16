class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if half != total / 2:
            return False
        
        memo = {}

        def dfs(i, res):
            if i == len(nums) or res > half:
                return False
            if res == half:
                return True

            if (i, res) in memo:
                return memo[(i, res)]

            take = dfs(i+1, res + nums[i])
            skip = dfs(i+1, res)
            memo[(i, res)] = take or skip
            return memo[(i, res)]
        
        return dfs(0, 0)