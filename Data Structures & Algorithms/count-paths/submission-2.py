class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        i, j = 0,0
        grid = [[-1]*cols for i in range(m)]
        
        def dfs(rows, cols, r,c, grid):
            if r == rows or c == cols:
                return 0
            if grid[r][c] != -1:
                return grid[r][c]
            if r == rows-1 and c == cols-1:
                return 1
            grid[r][c] = dfs(rows, cols, r+1, c, grid) + dfs(rows, cols, r, c + 1, grid)
            return grid[r][c]
        
        return dfs(rows, cols, 0,0, grid)