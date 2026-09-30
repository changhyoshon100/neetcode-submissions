class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,p in times:
            mp[s].append([d,p])
        visit = set()
        res = 0
        minHeap = [(0,k)]
        heapq.heapify(minHeap)

        while minHeap:
            time, loc = heapq.heappop(minHeap)
            if loc in visit:
                continue
            
            res = time
            visit.add(loc)
            
            for nei, t in mp[loc]:
                heapq.heappush(minHeap, (time + t, nei))
        return res if len(visit) == n else -1

            
