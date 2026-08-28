class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,w in times:
            mp[s].append((d,w))

        visit = set()
        
        minHeap = [(0,k)]
        res = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = w1
            for n2, w2 in mp[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))

        return res if n == len(visit) else -1
        





