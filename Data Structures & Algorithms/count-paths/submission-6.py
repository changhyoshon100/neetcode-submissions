class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(memo,i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            memo[i][j] = dfs(memo, i+1, j) + dfs(memo, i, j+1)
            return memo[i][j]
        return dfs(memo, 0,0)