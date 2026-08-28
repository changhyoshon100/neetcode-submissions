class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        minH = [(0,0)] # cost, point
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        visit = set()
        res = 0
        while len(visit) < len(points):
            cost, point = heapq.heappop(minH)
            if point in visit:
                continue
            res += cost
            visit.add(point)
            for c2, p2 in adj[point]:
                if p2 in visit:
                    continue
                heapq.heappush(minH, (c2, p2))
        return res

                

            