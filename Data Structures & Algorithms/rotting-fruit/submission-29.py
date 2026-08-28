class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i,j])
        time = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        
        while queue:
            
            for i in range(len(queue)):
                x,y = queue.popleft()
                
                for dx, dy in direction:
                    x_d = x + dx
                    y_d = y + dy
                    if (x_d < 0 or x_d >= ROWS) or (y_d < 0 or y_d >= COLS) or (x_d, y_d) in visit or grid[x_d][y_d] == 0 or grid[x_d][y_d] == 2:
                        continue
                    visit.add((x_d, y_d))
                    queue.append([x_d, y_d])
                    grid[x_d][y_d] = 2
            time += 1
        flag = False
        for i in range(ROWS):
            for j in range(COLS):
                
                if grid[i][j] == 2:
                    flag = True
                    continue
                elif grid[i][j] == 1:
                    return -1
        for i in range(ROWS):
            for j in range(COLS):
                if not flag and grid[i][j] == 0:
                    return 0
                
        
        return time - 1


                
