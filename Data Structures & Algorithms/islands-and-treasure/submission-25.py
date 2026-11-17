class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        trs = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    trs.append((r,c))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while trs:
            r,c = trs.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                trs.append((nr, nc))
        


                
