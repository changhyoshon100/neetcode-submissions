class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    queue.append((r,c,0))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]    
        while queue:
            for i in range(len(queue)):
                r,c,dist = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr,nc) in visit or grid[nr][nc] == -1 or grid[nr][nc] < dist:
                        continue
                    visit.add((nr,nc))
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc, grid[nr][nc]))
                

            
        
        