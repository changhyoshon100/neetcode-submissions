class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        
        for i in range(len(edges)):
            src, dst, sp = edges[i][0], edges[i][1], succProb[i]
            adj[src].append([dst, sp])
            adj[dst].append([src, sp])
        visit = set()
        pq = [[-1, start]]

        while pq:
            probs, curr = heapq.heappop(pq)
            visit.add(curr)
            if curr == end:
                return probs*-1
            for nei, pr in adj[curr]:
                if nei not in visit:
                    heapq.heappush(pq, [probs * pr, nei])
        return 0
            
            
