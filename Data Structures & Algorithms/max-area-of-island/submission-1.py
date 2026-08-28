class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        max_cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_cnt = max(max_cnt, self.dfs(grid, i,j, 0))
                
        return max_cnt

    def dfs(self, grid,i,j,cnt):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        elif grid[i][j] == 1:
            grid[i][j] = 0
            
            return (1 + self.dfs(grid,i-1,j,cnt)
            + self.dfs(grid,i+1,j,cnt)
            + self.dfs(grid,i,j-1,cnt)
            + self.dfs(grid,i,j+1,cnt)
            )
        
        