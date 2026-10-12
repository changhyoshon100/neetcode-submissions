class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(matrix), len(matrix[0])
        res = 0
        queue = deque()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or matrix[r][c] >= matrix[nr][nc]:
                    continue
                res = max(res, 1 + dfs(nr, nc))
            memo[(r,c)] = res
            return memo[(r,c)]

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r,c))
        return ans
        