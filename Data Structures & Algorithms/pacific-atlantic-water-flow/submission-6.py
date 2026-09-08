class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        queue_pac = deque()
        queue_atl = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.add((r,c))
                    queue_pac.append((r,c, heights[r][c]))
                if r == ROWS - 1 or c == COLS - 1:
                    atl.add((r,c))
                    queue_atl.append((r,c, heights[r][c]))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while queue_pac:
            r,c,h = queue_pac.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in pac or heights[nr][nc] < heights[r][c]:
                    continue
                queue_pac.append((nr, nc, heights[nr][nc]))
                pac.add((nr, nc))
        
        

        while queue_atl:
            r,c,h = queue_atl.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in atl or heights[nr][nc] < heights[r][c]:
                    continue
                queue_atl.append((nr, nc, heights[nr][nc]))
                atl.add((nr, nc))
        
        # print(atl)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

        
        
        
