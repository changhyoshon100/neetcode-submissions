class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        memo = {}

        def dfs(i, res):
            if i < 1:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in memo:
                return memo[i]
            res = dfs(i-1, res) + dfs(i-2, res)
            memo[i] = res
            
            return res
        
        return dfs(n, res)