class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visit = set()
        def dfs(grid, i, j):
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or (grid[i][j] == '0') or (i,j) in visit:
                return 0
            
            visit.add((i,j))
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

            return 1


        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                cnt += dfs(grid, i, j)
        return cnt