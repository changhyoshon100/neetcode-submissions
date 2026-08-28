class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r,c,prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or prev >= matrix[r][c]:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            val = 1 + max(
                    dfs(r+1,c,matrix[r][c]),
                dfs(r-1,c,matrix[r][c]),
                dfs(r,c+1,matrix[r][c]),
                dfs(r,c-1,matrix[r][c])
            )
            memo[(r,c)] = val
        
            return memo[(r,c)]        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c,-1))
        return res
