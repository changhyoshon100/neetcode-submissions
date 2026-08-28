class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        origin = []
        path = set()
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    origin.append((r,c))

        def dfs(r,c,area):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in path or grid[r][c] == 0: 
                return 0
            
            path.add((r,c))
            
            area = (dfs(r+1,c, area)+
            dfs(r-1,c, area)+
            dfs(r,c+1, area)+
            dfs(r,c-1, area)) + 1
            return area

        for r,c in origin:
            res = max(res, dfs(r,c,0))
            
        return res