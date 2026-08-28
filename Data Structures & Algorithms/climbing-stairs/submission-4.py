class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(n,cache):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = dfs(n-1,cache) + dfs(n-2,cache)
            return cache[n]
        return dfs(n, cache)
        