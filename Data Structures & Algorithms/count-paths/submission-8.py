class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        
        memo = {}
        def dfs(i,j,res):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return 0
            if i == ROWS - 1 and j == COLS - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dfs(i+1,j,res) + dfs(i,j+1,res)
            return memo[(i,j)]
        return dfs(0,0,0)
