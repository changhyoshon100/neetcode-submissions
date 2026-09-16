class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        memo = {}
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            
            best = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if matrix[r][c] < matrix[nr][nc]:
                    best = max(best, 1 + dfs(nr, nc))
                    
            memo[(r,c)] = best
            return memo[(r,c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c)
        return max(memo.values())