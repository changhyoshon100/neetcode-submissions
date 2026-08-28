class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direction = [[0,-1],[0,1],[1,0],[-1,0]]
        minH = [[grid[0][0], 0,0]]
        visit = set()
        visit.add((0,0))
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in direction:
                neiR, neiC = r + dr, c + dc
                if (neiR,neiC) in visit or neiR < 0 or neiR >= N or neiC < 0 or neiC >= N:
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
                
