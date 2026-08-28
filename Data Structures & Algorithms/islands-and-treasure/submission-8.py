class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        origin = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    origin.append((r,c))
        cnt = 0
        def dfs(r,c,cnt, path):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r,c) in path or cnt > grid[r][c]:
                return

            path.add((r,c))
            if grid[r][c] != -1 or grid[r][c] != 0:
                grid[r][c] = min(cnt, grid[r][c])
            dfs(r+1,c, cnt + 1, path)
            dfs(r-1,c, cnt + 1, path)
            dfs(r,c+1, cnt + 1, path)
            dfs(r,c-1, cnt + 1, path)
            path.remove((r,c))

        for r,c in origin:
            dfs(r,c,0, set())
