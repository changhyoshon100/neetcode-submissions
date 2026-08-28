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
            a = dfs(r + 1, c) 
            b = dfs(r, c + 1)
            memo[(r,c)] = a + b
            return memo[(r,c)]
        
        return dfs(0,0)