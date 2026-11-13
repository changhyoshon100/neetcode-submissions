class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,p in times:
            mp[s].append((p,d))

        minH = [(0, k)]
        visited = set()
        res = 0
        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            
            visited.add(n1)
            res = w1
            
            for w2, n2 in mp[n1]:
                heapq.heappush(minH, (w1 + w2, n2))
        return res if len(visited) == n else -1


