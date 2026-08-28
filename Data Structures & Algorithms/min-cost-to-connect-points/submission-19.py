class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mp = defaultdict(list)
        
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                mp[i].append((j, dist))
                mp[j].append((i, dist))
        # dist, start
        minHeap = [(0,0)]
        visit = set()
        
        res = 0
        while minHeap:
            d1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            res += d1
            visit.add(n1)
            for n2, d2 in mp[n1]:
                heapq.heappush(minHeap, (d2, n2))
        return res
            

