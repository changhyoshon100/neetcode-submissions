class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        def dfs(r,c,prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0
        
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            memo[(r,c)] = 1 + max(
                    dfs(r+1,c, matrix[r][c]),
                dfs(r-1,c, matrix[r][c]),
                dfs(r,c+1, matrix[r][c]),
                dfs(r,c-1, matrix[r][c])
            )
            
            return memo[(r,c)]
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j,-1))
        return res