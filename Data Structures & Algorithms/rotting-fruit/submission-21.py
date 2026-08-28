class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        check_remain = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    check_remain.add((i,j))
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        
        if not check_remain:
            return 0
        if len(queue) == 0:
            return -1
        adjacent = [(0,-1),(0,1),(1,0),(-1,0)]
        cnt = 0
        
        while queue and check_remain:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in adjacent:
                    x_d = x + dx
                    y_d = y + dy
                    if 0 <= x_d < len(grid) and 0 <= y_d < len(grid[0]) and grid[x_d][y_d] == 1:
                        queue.append((x_d,y_d))
                        check_remain.remove((x_d,y_d))
                        grid[x_d][y_d] = 2
            cnt += 1
                    
        if check_remain:
            return -1
        return cnt
                    

            
        
