class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = set()
        atl = set()
        queuePac = deque()
        queueAtl = deque()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    queuePac.append((r,c))
                    pac.add((r,c))
                if r == ROWS - 1 or c == COLS - 1:
                    queueAtl.append((r,c))
                    atl.add((r,c))
        
        def bfs(queue, mp):
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or heights[r][c] > heights[nr][nc]:
                        continue
                    if (nr, nc) in mp:
                        continue
                    mp.add((nr, nc))
                    queue.append((nr, nc))
            

        ans = []
        bfs(queuePac, pac)
        bfs(queueAtl, atl)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    ans.append((r,c))
        return ans



            
        
                
        

        
