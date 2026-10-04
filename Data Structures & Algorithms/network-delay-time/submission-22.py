class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        
        for s,d,w in times:
            mp[s].append((w,d))

        visited = set()
        minH = [(0, k)]
        res = 0
        while minH:
            w1, n1 = heapq.heappop(minH)
            if n1 in visited:
                continue
            res = w1            
            visited.add(n1)
            for w2, n2 in mp[n1]:
                heapq.heappush(minH, (w1 + w2, n2))

        return res if len(visited) == n else -1