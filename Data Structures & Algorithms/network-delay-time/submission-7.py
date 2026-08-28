class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        edges = {i:[] for i in range(1,n+1)}
        minHeap = [(0,k)] # weight, node
        for i,v,w in times:
            edges[i].append([w,v])
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for w2, n2 in edges[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(minHeap, (w1+w2, n2))
        return t if len(visit) == n else -1 
            

