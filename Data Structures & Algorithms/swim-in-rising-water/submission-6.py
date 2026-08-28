class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        visit.add((0,0))
        minH = [[grid[0][0], 0, 0]]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == ROWS - 1 and c == COLS - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                
                if neiR < 0 or neiR >= ROWS or neiC < 0 or neiC >= COLS or (neiR, neiC) in visit:
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]),neiR, neiC])
        

            
        