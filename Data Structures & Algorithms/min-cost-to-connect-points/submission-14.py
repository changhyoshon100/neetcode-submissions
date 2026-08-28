class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        res = 0
        mp = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1-x2) + abs(y1-y2)
                mp[i].append([j,dist])
                mp[j].append([i,dist])
        
        # dist, node
        minHeap = [(0,0)]
        res = 0
        while minHeap:
            d1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res += d1
            for n2, d2 in mp[n1]:
                heapq.heappush(minHeap, (d2, n2))
        return res
        