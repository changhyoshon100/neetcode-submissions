class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        res = 0
        def dfs(grid,i,j):
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or grid[i][j] == 0 or (i,j) in visit:
                return 0
            
            visit.add((i,j))
            cnt = 1
            cnt += dfs(grid,i-1,j)
            cnt += dfs(grid,i+1,j)
            cnt += dfs(grid,i,j-1)
            cnt += dfs(grid,i,j+1)

            return cnt 
        
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(grid,i,j))
        return res