class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()
        # visit = set()
        r,c = 0,0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    r,c = i,j
                    queue.append((r,c))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        # queue.append((r,c))
        # visit.add((r,c))
        neighbors = [[0,1],[0,-1],[-1,0],[1,0]]
        length = 0
        if len(queue) == 0:
            return -1
        while fresh > 0 and queue:
            leng = len(queue)
            for i in range(leng):
                print(fresh, length,queue)
                r,c = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    print(nr,nc)
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    
                    queue.append((nr,nc))
                    print(queue)
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    
            length += 1
        print(fresh)
        return length if fresh == 0 else -1




            
            

                    

