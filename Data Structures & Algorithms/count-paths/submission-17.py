class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m,n
        memo = {}
        def dfs(r,c):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = dfs(r+1, c) + dfs(r, c+1)
            return memo[(r,c)]
        return dfs(0,0)