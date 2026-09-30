class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        visit = set()
        for s,d,w in times:
            mp[s].append([d,w])
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        res = 0
        while minHeap:
            time, loc = heapq.heappop(minHeap)
            if loc in visit:
                continue
            visit.add(loc)
            res = time
            for nei, t in mp[loc]:
                heapq.heappush(minHeap, (time + t, nei))
        return res if len(visit) == n else -1
