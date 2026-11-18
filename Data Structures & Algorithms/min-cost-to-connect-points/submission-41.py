class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        mp = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                mp[i].append((dist, j))
                mp[j].append((dist, i))

        # dist, node
        minH = [(0,0)]
        res = 0
        while minH:
            d1, n1 = heapq.heappop(minH)
            if len(visit) == len(points):
                return res
            if n1 in visit:
                continue
            visit.add(n1)
            res += d1
            for d2, n2 in mp[n1]:
                heapq.heappush(minH, (d2, n2))
        return 0
            




        