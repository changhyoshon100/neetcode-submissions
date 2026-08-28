class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_cnt = 0
        cnt = 0
        def dfs(r,c,cnt):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return cnt
            
            if grid[r][c] == 0:
                return cnt
            elif grid[r][c] == 1:
                cnt += 1
                
                grid[r][c] = 0
                cnt = dfs(r+1, c,cnt)
                cnt = dfs(r-1, c,cnt)
                cnt = dfs(r, c+1,cnt)
                cnt = dfs(r, c-1,cnt)
                
                return cnt

        for r in range(rows):
            for c in range(cols):
                max_cnt = max(max_cnt, dfs(r,c,cnt))
                    
        return max_cnt
