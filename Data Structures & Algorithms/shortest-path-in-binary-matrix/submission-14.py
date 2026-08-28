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
        flag = False
        while queue:
            
            for i in range(len(queue)):
                x,y = queue.popleft()
                
                if x == ROWS - 1 and y == COLS - 1:
                    flag = True
                    return length
                for dx,dy in direction:
                    x_d = x + dx
                    y_d = y + dy
                    
                    if (x_d < 0 or x_d >= ROWS) or (y_d < 0 or y_d >= COLS) or (grid[x_d][y_d] == 1) or (x_d, y_d) in visit:
                        continue
                    
                    visit.add((x_d, y_d))
                    queue.append([x_d, y_d])
            length += 1
        if not flag: return -1
        return length


            