class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        dp = [1] * n
        
        for r in range(rows-2,-1,-1):
            for c in range(cols-2, -1, -1):
                dp[c] += dp[c+1]
        return dp[0]
