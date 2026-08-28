class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        

        def dfs(r,c):
            nonlocal res
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or (r,c) in path:
                return 0

            path.add((r,c))
            
            res += 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return res
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = 0
                ans = max(ans, dfs(r,c))
        return ans
        