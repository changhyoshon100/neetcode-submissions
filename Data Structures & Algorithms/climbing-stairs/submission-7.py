class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        cache = {}
        def dfs(n):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = dfs(n-1) + dfs(n-2)
            return cache[n]
        return dfs(n)
            
