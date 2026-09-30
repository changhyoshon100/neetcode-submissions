class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        res = 0
        minHeap = []
        mp = defaultdict(list)
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                mp[i].append((dist,j))
                mp[j].append((dist,i))
        minHeap = [(0,0)]
        heapq.heapify(minHeap)

        while minHeap:
            dist, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            res += dist
            visit.add(n1)
            
            for dist, nei in mp[n1]:
                heapq.heappush(minHeap, (dist, nei))
        return res

                


                