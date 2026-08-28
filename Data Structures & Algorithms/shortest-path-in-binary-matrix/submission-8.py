class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))
        adjacent = [(0,-1),(0,1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        grid[0][0] = 1
        
        while queue:
            x,y = queue.popleft()
            cnt = grid[x][y]
            for dx, dy in adjacent:
                x_d = x + dx
                y_d = y + dy
                if x_d == len(grid) - 1 and y_d == len(grid) - 1:
                    return cnt + 1
                
                if 0 <= x_d < len(grid) and 0 <= y_d < len(grid) and grid[x_d][y_d] == 0 and (x_d, y_d) not in visited:
                    queue.append((x_d, y_d))
                    visited.add((x_d, y_d))
                    grid[x_d][y_d] = cnt + 1
            
        return -1
                





