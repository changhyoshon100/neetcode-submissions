class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        pacQueue = deque()
        atlQueue = deque()

        pacVisit = set()
        atlVisit = set()

        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pac.add((r,c))

                if r == ROWS - 1 or c == COLS - 1:
                    atl.add((r,c))

        def dfs(r, c, queue, visit):
            if (r,c) in queue:
                return 
            queue.append((r,c))
            visit.add((r,c))
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                            continue 
                        if (nr, nc) in visit:
                            continue
                        if heights[nr][nc] >= heights[r][c]:
                            queue.append((nr,nc))
                            visit.add((nr,nc))

        for r,c in pac:
            dfs(r,c,pacQueue,pacVisit)
        for r,c in atl:
            dfs(r,c,atlQueue,atlVisit)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacVisit and (r,c) in atlVisit:
                    res.append((r,c))
        return res


        