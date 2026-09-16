class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(matrix), len(matrix[0])
       
        def dfs(r,c,curr):
            if (r,c) in memo:
                return memo[(r,c)]
            best = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0: 
                    continue
                new_curr = matrix[nr][nc]
                if new_curr > curr:
                    best = max(best, 1 + dfs(nr, nc, new_curr))
            memo[(r,c)] = best
            return best
            
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,matrix[i][j])
        
        return max(memo.values())
