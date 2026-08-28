class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    cnt += 1
        print(queue)
        if not queue and cnt > 0:
            return -1
        elif not queue and cnt == 0:
            return 0
        
        visit = set()
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        time = 0
        while queue:
            for i in range(len(queue)):
                print(queue,time)
                if not queue:
                    return time
                x,y = queue.popleft()
                for dx, dy in direction:
                    x_, y_ = x + dx, y + dy
                    if (x_ < 0 or x_ >= ROWS) or (y_ < 0 or y_ >= COLS) or (x_,y_) in visit or grid[x_][y_] == 0 or grid[x_][y_] == 2:
                        continue
                    grid[x_][y_] = 2
                    visit.add((x_,y_))
                    queue.append([x_,y_])

            time += 1
        for i in range(ROWS):
            if 1 in grid[i]:
                return -1
        return time - 1



        
