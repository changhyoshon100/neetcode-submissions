class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mp = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                mp[i].append((j,dist))
                mp[j].append((i,dist))
        
        visited = set()
        minH = [(0,0)]
        heapq.heapify(minH)
        res = 0
        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            visited.add(n1)
            res += w1
            for n2, w2 in mp[n1]:
                heapq.heappush(minH, (w2, n2))
        return res