class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows = len(grid)
        cols = len(grid[0])
        cache = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c):
            if r >= rows or c >= cols or grid[r][c]:
                return 0
            if r == rows - 1 and c == cols - 1:
                cache[r][c] = 1
                return 1
            if cache[r][c] != -1:
                return cache[r][c]

            cache[r][c] = dfs(r+1,c) + dfs(r, c+1)
            return cache[r][c]
        return dfs(0,0)
        
        
