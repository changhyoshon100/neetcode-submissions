class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        def dfs(i,j,grid,count):
            if (i,j) in visit or (i < 0 or i >= ROWS) or (j < 0 or j >= COLS) or grid[i][j] == '0':
                return 0
            
            visit.add((i,j))
            
            count += dfs(i+1,j,grid,count)
            count += dfs(i-1,j,grid,count)
            count += dfs(i,j+1,grid,count)
            count += dfs(i,j-1,grid,count)

            return 1
            

            
        for i in range(ROWS):
            for j in range(COLS):
                res += dfs(i,j,grid,0)
        return res