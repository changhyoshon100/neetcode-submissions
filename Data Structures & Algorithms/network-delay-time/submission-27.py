class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,p in times:
            mp[s].append((d,p))
        
        visited = set()
        minH = [(0, k)]
        heapq.heapify(minH)
        res = 0
        
        while minH:
            w1, n1 = heapq.heappop(minH)
            res = w1
            if n1 in visited:
                continue
            visited.add(n1)
            if len(visited) == n:
                return res
            
            for n2, w2 in mp[n1]:  
                heapq.heappush(minH, (w1 + w2, n2))
        # print(visited)
        return res if len(visited) == n else -1