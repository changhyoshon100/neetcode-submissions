class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mp = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                mp[i].append((dist,j))
                mp[j].append((dist,i))
        
        minH = [(0,0)]
        visited = set()
        # visited.add(0)
        res = 0
        while minH:
            w1, n1 = heapq.heappop(minH)
            if len(visited) == len(points):
                return res
            if n1 in visited:
                continue
            visited.add(n1)
            res += w1
            
            for w2, n2 in mp[n1]:
                heapq.heappush(minH, (w2, n2))
        
        return 0


