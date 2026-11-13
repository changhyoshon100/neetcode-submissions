class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        mp = defaultdict(list)
        for i in range(len(points)):
            p = points[i]
            for j in range(i+1, len(points)):
                q = points[j]
                dist = abs(p[0] - q[0]) + abs(p[1] - q[1])
                mp[i].append((dist, j))
                mp[j].append((dist, i))
        
        minH = []
        minH.append((0, 0))
        res = 0
        visited = set()
        while minH:
            d1, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            if len(visited) == len(points):
                return res
            visited.add((n1))
            res += d1
            for d2, n2 in mp[n1]:
                heapq.heappush(minH, (d2, n2))
        return res
        




                