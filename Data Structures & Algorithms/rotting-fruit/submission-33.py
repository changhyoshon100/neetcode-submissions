class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = -1
        while q:
            time += 1
            # print(time, q)
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    
                    neiR, neiC = r + dr, c + dc
                    if neiR < 0 or neiR >= ROWS or neiC < 0 or neiC >= COLS or (neiR,neiC) in visit or grid[neiR][neiC] != 1:
                        continue
                    fresh -= 1
                    visit.add((neiR,neiC))
                    q.append([neiR,neiC])
        
        return time if fresh == 0 else -1
