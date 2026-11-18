class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for s,d,w in times:
            mp[s].append((w,d))
        
        minH = []
        minH.append((0,k))
        res = 0
        visit = set()
        
        while minH:
            w1, n1 = heapq.heappop(minH)

            if n1 in visit:
                continue
            visit.add(n1)
            res = w1
            
            for w2, n2 in mp[n1]:
                heapq.heappush(minH, (w1 + w2, n2))
        
        return -1 if len(visit) != n else res
                    
                

            
