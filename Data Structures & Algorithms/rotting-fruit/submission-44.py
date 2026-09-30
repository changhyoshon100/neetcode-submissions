class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        fresh = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c,time))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        if not fresh: return 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue:
            for i in range(len(queue)):
                r,c,time = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr,nc) in visit or grid[nr][nc] == 0:
                        continue
                    
                    visit.add((nr,nc))
                    grid[nr][nc] = 2
                    queue.append((nr,nc,time+1))
                    fresh -= 1
            
        return time if fresh == 0 else -1

                
            


