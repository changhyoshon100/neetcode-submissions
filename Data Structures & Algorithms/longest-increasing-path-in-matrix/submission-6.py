class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        # visit = set()
        def dfs(r,c,val):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= val:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            # visit.add((r,c))
            total = 0
            if val < matrix[r][c]:
                total = 1
            
            total += max(dfs(r+1,c, matrix[r][c]),
                dfs(r-1,c, matrix[r][c]),
                dfs(r,c+1, matrix[r][c]),
                dfs(r,c-1, matrix[r][c]))
            memo[(r,c)] = total
            # visit.remove((r,c))
            return memo[(r,c)]
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r,c,-1))
        return ans
        