class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        cnt = 0
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == '0':
                return False

            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c):
                    cnt += 1
                
        return cnt
                    