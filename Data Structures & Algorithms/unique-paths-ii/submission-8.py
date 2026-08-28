class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        r = len(grid)
        c = len(grid[0])
        cache = [[-1 for i in range(c)] for j in range(r)]
        print(cache)
        def dfs(i,j):
            if i >= r  or j >= c:
                return 0
            if grid[i][j] == 1:
                return 0
            if i == r-1 and j == c-1:
                return 1
            if cache[i][j] != -1:
                return cache[i][j]
            
            cache[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return cache[i][j]
        
        return dfs(0,0)