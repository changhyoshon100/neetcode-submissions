class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mp = defaultdict(list)
        res = 0
        minHeap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                mp[i].append((j, dist))
                mp[j].append((i, dist))
        
        # d, i
        minHeap.append((0,0))
        visit = set()
        while minHeap:
            d,i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res += d
            for j, d2 in mp[i]:
                heapq.heappush(minHeap,(d2, j))
        return res
            




                