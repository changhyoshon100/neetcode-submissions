class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        res = 0
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in path or grid[r][c] == '0':
                return 0
            
            path.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c) 
            dfs(r,c+1)
            dfs(r,c-1)
            return 1


        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r,c)
        return res