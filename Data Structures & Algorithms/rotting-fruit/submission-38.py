class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        if fresh == 0: return 0
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    fresh -= 1
                    
            time += 1
        if fresh:
            return -1
        return time - 1
        
                


        