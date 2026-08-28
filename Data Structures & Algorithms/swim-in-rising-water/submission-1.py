class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        visit.add((0,0))
        minH = [[grid[0][0], 0, 0]]
        N = len(grid)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            t,r,c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr,dc in directions:                
                neiR = r + dr
                neiC = c + dc
                if neiR == N or neiC == N or (neiR, neiC) in visit or neiR < 0 or neiC < 0:
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR,neiC])
        
            