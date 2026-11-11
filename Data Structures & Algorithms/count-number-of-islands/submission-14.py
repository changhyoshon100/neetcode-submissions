class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if not (0 <= r < ROWS and 0 <= c < COLS):  
                return 0
            if (r,c) in visited or grid[r][c] == "0":
                return 0
            
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return 1
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    res += dfs(r,c)
                    
        
        return res
