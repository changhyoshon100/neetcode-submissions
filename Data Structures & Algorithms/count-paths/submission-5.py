class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 and n <= 1:
            return 1
        cache = [[0 for i in range(n)] for i in range(m)]

        def dfs(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if cache[i][j]:
                return cache[i][j]
            
            cache[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return cache[i][j]

        dfs(0,0)
        return cache[0][0]
        