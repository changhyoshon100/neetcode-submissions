class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        minHeap = [(0,k)]
        adj = {i:[] for i in range(1,n+1)}
        for i,v,w in times:
            adj[i].append([v,w])
            
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in adj[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minHeap,(w1 + w2, n2))
        return t if len(visit) == n else -1



