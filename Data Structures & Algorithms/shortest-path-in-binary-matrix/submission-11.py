class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        direction = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        queue = deque()
        queue.append([0,0])
        length = 1
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        visit.add((0,0))
        grid[0][0] = 1
        while queue:
            for i in range(len(queue)):
                x,y = queue.popleft()
                if x == ROWS - 1 and y == COLS - 1:
                        return length

                for dx, dy in direction:
                    x_mv = x + dx
                    y_mv = y + dy
                    if (x_mv < 0 or x_mv >= ROWS) or (y_mv < 0 or y_mv >= COLS) or (x_mv, y_mv) in visit or grid[x_mv][y_mv] == 1:
                        continue
                    visit.add((x_mv, y_mv))
                    queue.append([x_mv, y_mv])
            length += 1
                
        return -1


