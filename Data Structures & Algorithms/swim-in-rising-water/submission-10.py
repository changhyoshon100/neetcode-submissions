class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        minHeap = [(grid[0][0],0,0)]
        visit = set()
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        res = 0
        while minHeap:
            h,r,c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            res = h
            if r == ROWS - 1 and c == COLS - 1:
                return res
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit:
                    continue
                heapq.heappush(minHeap, (max(h, grid[nr][nc]), nr, nc))
        


