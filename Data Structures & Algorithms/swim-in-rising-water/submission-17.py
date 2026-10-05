class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        minHeap = [(grid[0][0],0,0)] 
        visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while minHeap:
            h,r,c = heapq.heappop(minHeap) # time: log MN where M is row and N is col
            if r == ROWS - 1 and c == COLS - 1:
                return h
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited:
                    continue
                visited.add((nr,nc)) # space: MN
                heapq.heappush(minHeap, ((max(h, grid[nr][nc]), nr,nc)))
        # time: each time takes log MN and the grid size is MN -> MN * log MN
        # space: MN
