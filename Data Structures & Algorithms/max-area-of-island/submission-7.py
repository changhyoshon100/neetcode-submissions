class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def dfs(r,c,cnt):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            

            return 1 + dfs(r+1,c,cnt) + dfs(r-1,c,cnt) + dfs(r,c+1,cnt) + dfs(r,c-1,cnt)
            
        maxCnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxCnt = max(maxCnt, dfs(r,c,0))
        return maxCnt