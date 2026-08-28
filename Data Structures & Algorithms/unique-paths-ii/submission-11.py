class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        grid = obstacleGrid
        ROWS, COLS = len(grid), len(grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]
        def dfs(grid,i,j,res):
            if i >= ROWS or j >= COLS:
                return 0
            
            if grid[i][j] == 1:
                return 0
            
            if i == ROWS-1 and j == COLS-1:
                return 1

            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(grid,i+1,j,res) + dfs(grid,i,j+1,res)
            
            return memo[i][j]
    
        return dfs(grid,0,0,0)
