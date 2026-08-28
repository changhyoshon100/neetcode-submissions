class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        minHeap = [(grid[0][0],0,0)]
        visit = set()
        res = 0
        while minHeap:
            h,r,c = heapq.heappop(minHeap)
            res = h
            if r == ROWS - 1 and c == COLS - 1:
                return res
            
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap, (max(res, grid[nr][nc]), nr, nc))
        return res

