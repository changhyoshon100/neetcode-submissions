class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0],0,0)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        while minHeap:
            h,r,c = heapq.heappop(minHeap)
            res = h
            if r == ROWS - 1 and c == COLS - 1:
                return res

            if (r,c) in visit:
                continue
            visit.add((r,c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit:
                    continue
                heapq.heappush(minHeap, (max(h, grid[nr][nc]), nr,nc))
            
            