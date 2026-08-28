class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        R = len(grid)
        C = len(grid)
        visit.add((0,0))
        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if r == R - 1 and c == C - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR == R or neiC == C or neiR < 0 or neiC < 0 or (neiR,neiC) in visit):
                    continue
                visit.add((neiR,neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
        t,r,c = heapq.heappop(minHeap)
        return t
        