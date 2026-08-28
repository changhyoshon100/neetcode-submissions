class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0
        
        directory = [[-1,0],[1,0],[0,-1],[0,1]]
        cnt = -1

        while q:
            
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directory:
                    r2 = r + dr
                    c2 = c + dc
                    if r2 < 0 or r2 >= ROWS or c2 < 0 or c2 >= COLS or grid[r2][c2] == 0 or grid[r2][c2] == 2:
                        continue
                    if grid[r2][c2] == 1:
                        q.append([r2,c2])
                    grid[r2][c2] = 2
                    fresh -= 1
            cnt += 1
        
        return cnt if fresh == 0 else -1
