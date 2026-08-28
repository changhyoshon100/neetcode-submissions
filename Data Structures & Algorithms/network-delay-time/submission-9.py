class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for u,v,w in times:
            mp[u].append((v,w))
        # weight, initial node
        minHeap = [(0, k)]
        visit = set()
        time = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            time = w1
            for n2, w2 in mp[n1]:
                heapq.heappush(minHeap, (w1 + w2, n2))
        return time if len(visit) == n else -1
            

        