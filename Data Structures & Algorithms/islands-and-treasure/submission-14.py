class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure.append((r,c))

        visited = set()
        memo = {}
        def dfs(r,c,dist):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r,c) in visited or dist > grid[r][c]:
                return 
            
            visited.add((r,c))
            grid[r][c] = min(dist, grid[r][c])
            

            dist += 1
            dfs(r+1,c,dist)
            dfs(r-1,c,dist)
            dfs(r,c+1,dist)
            dfs(r,c-1,dist)
            memo[(r,c)] = dist
            visited.remove((r,c))

        for r,c in treasure:
            dfs(r,c,0)