class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        init = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    init.add((r,c))
        
        def dfs(grid, r, c, dist):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or dist > grid[r][c]:
                return

            grid[r][c] = dist
            
            
            dfs(grid, r+1, c, dist + 1)
            dfs(grid, r-1, c, dist + 1)
            dfs(grid, r, c+1, dist + 1)
            dfs(grid, r, c-1, dist + 1)
            # visit.remove((pr,pc))
        
        for i in range(len(init)):
            dfs(grid, list(init)[i][0], list(init)[i][1], 0)

