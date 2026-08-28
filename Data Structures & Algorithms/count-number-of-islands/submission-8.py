class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        res = 0
        origin = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    origin.append((r,c))
        
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in path or grid[r][c] == '0':
                return 
                
            path.add((r,c))
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return True

        for r,c in origin:
            if dfs(r,c):
                res += 1
        return res