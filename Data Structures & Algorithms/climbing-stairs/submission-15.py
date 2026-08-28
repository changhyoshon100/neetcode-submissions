class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i,res):            
            if i == 1:
                res = 1
                return res
            if i == 2:
                res = 2
                return res
            if i in memo:
                return memo[i]
            
            res = dfs(i-1, res) + dfs(i-2, res)
            memo[i] = res
            return res
        return dfs(n,0)