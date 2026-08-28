class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        rows = len(grid)
        cols = len(grid[0])
        cache = [[-1 for _ in range(cols)] for _ in range(rows)]
        print(cache)
        def dfs(r,c):
            if r == rows or c == cols:
                return 0
            if grid[r][c] == 1:
                cache[r][c] = 0
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                cache[r][c] = 1
                return 1
            cache[r][c] = dfs(r+1,c) + dfs(r,c+1)
            return cache[r][c]
        
        return dfs(0,0)