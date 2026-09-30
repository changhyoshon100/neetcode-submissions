class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = deque()
        atl = deque()
        visit_pac = set()
        visit_atl = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.append((r,c, heights[r][c]))
                    visit_pac.add((r,c))
                if r == ROWS - 1 or c == COLS - 1:
                    atl.append((r,c, heights[r][c]))
                    visit_atl.add((r,c))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def bfs(queue, visit):
            while queue:
                r,c,h = queue.popleft()                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visit or heights[nr][nc] < h:
                        continue
                    visit.add((nr,nc))
                    queue.append((nr,nc,heights[nr][nc]))
                
        bfs(pac, visit_pac)        
        bfs(atl, visit_atl)
        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visit_pac and (r,c) in visit_atl:
                    res.append((r,c))
        return res






