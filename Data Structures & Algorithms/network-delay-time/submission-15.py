class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        minHeap = [(0,k)]
        visit = set()

        mp = defaultdict(list)
        for s,d,p in times:
            mp[s].append((d,p))
        res = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            res = w1
            visit.add(n1)
            for n2, w2 in mp[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))
        return res if len(visit) == n else -1


