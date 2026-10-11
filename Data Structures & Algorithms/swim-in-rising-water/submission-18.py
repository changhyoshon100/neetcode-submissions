class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        # r,c
        minH = [(grid[0][0],0,0)]
        visited = set()
        res = 0
        while minH:
            h,r,c = heapq.heappop(minH)
            if r == ROWS - 1 and c == COLS - 1:
                return h
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                visited.add((nr,nc))
                heapq.heappush(minH, (max(h, grid[nr][nc]), nr, nc))
                
                
