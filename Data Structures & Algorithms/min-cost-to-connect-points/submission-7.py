class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(points)-1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visit = set()
        minHeap = [(0,0)] # dist, point
        total = 0

        while len(visit) < len(points):
            if not minHeap:
                return 0
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            total += dist
            for nei_dist, neighbor in adj[point]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, (nei_dist, neighbor))
        return total

        
