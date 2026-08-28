class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pac = deque()
        atl = deque()
        visited_pac = set()
        visited_atl = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.append((r,c))
                    visited_pac.add((r,c))
                if r == ROWS - 1 or c == COLS - 1:
                    atl.append((r,c))
                    visited_atl.add((r,c))

        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        def bfs(q, visited):
            while q:
                r,c = q.popleft()
               
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or heights[nr][nc] < heights[r][c] or (nr,nc) in visited:
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
        
        bfs(pac, visited_pac)
        bfs(atl, visited_atl)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited_pac and (r,c) in visited_atl:
                    res.append([r,c])
        return res


                




