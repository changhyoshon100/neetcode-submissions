class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,p in times:
            mp[s].append((p,d))
        
        minHeap = [(0,k)]
        visited = set()
        res = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            res = t1
            visited.add(n1)

            for t2, n2 in mp[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))
        return res if len(visited) == n else -1

            