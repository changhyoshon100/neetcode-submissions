class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for u,v,w in times:
            mp[u].append((v,w))
            # mp[v].append((u,w))
        
        minHeap = [(0,k)]
        t = 0
        visit = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)
            for n2, w2 in mp[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1



