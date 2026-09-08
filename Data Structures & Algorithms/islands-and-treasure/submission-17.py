class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        dist = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c,dist])
        
        path = set()
        inf = 2147483647
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r,c,dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in path or grid[nr][nc] != inf:
                    continue
                path.add((nr, nc))
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = min(grid[nr][nc], dist + 1)




            
            
            
