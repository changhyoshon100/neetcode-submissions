class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or matrix[nr][nc] <= matrix[r][c]:
                    continue
                res = max(res, 1 + dfs(nr,nc))
            memo[(r,c)] = res
            return res
                

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r,c))
        return ans