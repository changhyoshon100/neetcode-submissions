class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] or grid[rows-1][cols-1]:
            return -1
        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))
        length = 1
        
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue

                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            length += 1
        return -1
                