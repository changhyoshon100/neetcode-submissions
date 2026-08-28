class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))
        neighbors = [[0,-1],[0,1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        length = 1

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == 1 or (nr,nc) in visit:
                        continue
                    
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1

