class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(n):
            if n == 1:
                return 1
            if n == 0:
                return 1
            return dfs(n-1) + dfs(n-2)
        return dfs(n)