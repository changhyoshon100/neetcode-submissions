class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        memo = {}

        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            length = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or matrix[nr][nc] <= matrix[r][c]:  
                    continue
                length = max(length, 1 + dfs(nr,nc))
            memo[(r,c)] = length
            return memo[(r,c)]

        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                answer = max(answer, dfs(r,c))
        return answer
