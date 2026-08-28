class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        largest = 0
        def dfs(grid, r, c):
            nonlocal res
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            res = dfs(grid, r-1, c) + dfs(grid, r+1, c) + dfs(grid, r, c-1) + dfs(grid, r, c+1) + 1
            return res
        
            
        for r in range(ROWS):
            for c in range(COLS):
                res += max(res, dfs(grid, r, c))
                largest = max(res, largest)
                res = 0
        return largest