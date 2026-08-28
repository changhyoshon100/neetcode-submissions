class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        for r in range(rows):
            for j in range(cols):
                if grid[r][j] == 2:
                    queue.append((r,j))
                if grid[r][j] == 1:
                    fresh += 1
        neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
        length = 0
        if fresh == 0:
            return 0
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    
                    
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh -= 1
                    
            length += 1
        if fresh == 0:
            return length
        else:
            return -1
                
                