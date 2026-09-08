class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0
        time = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in path or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))
                    path.add((nr, nc))
                    fresh -= 1
            time += 1
                
        if fresh != 0:
            return -1
        return time - 1

                



        
        

