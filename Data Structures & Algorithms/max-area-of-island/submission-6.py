class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        cntMax = 0
        cnt = 0
        
        def dfs(grid, i, j, cnt, cntMax):
            if (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or (i,j) in visit or grid[i][j] == 0:
                return 0

            cnt = 1
            visit.add((i,j))
            
            cnt += dfs(grid, i+1, j, cnt, cntMax)
            cnt += dfs(grid, i-1, j, cnt, cntMax)
            cnt += dfs(grid, i, j+1, cnt, cntMax)
            cnt += dfs(grid, i, j-1, cnt, cntMax)
            
            return cnt
            
        
        for i in range(ROWS):
            for j in range(COLS):
                cntMax = max(cntMax, dfs(grid, i, j, cnt, cntMax))
        return cntMax
                
