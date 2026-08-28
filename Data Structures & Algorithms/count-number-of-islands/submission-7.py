class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(grid, r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return False
            grid[r][c] = '0'
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)
            return True
            
            
        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(grid, r, c)
        return res