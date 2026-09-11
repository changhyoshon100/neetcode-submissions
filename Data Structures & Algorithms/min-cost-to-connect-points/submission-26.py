class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mp = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                mp[i].append((dist, j))
                mp[j].append((dist, i))

        minHeap = [(0, 0)]
        visit = set()
        res = 0
        while minHeap:
            d1, n1 = heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            res += d1
            visit.add(n1)
            
            for d2, n2 in mp[n1]:
                heapq.heappush(minHeap, (d2, n2))
        return res


