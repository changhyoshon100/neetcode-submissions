class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        minH = [(0,0,0)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = grid[0][0]
        while minH:
            h,r,c = heapq.heappop(minH)
            res = max(res, h)
            if r == ROWS - 1 and c == COLS - 1:
                return res
            
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit:
                    continue
                heapq.heappush(minH, (grid[nr][nc], nr, nc))
                visit.add((nr, nc))
                



