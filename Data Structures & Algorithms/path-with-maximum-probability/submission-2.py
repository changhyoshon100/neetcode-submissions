class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)

        for i in range(len(edges)):
            src, dst, sp = edges[i][0], edges[i][1], succProb[i]
            adj[src].append([dst, sp])
            adj[dst].append([src, sp])
        
        pq = [[-1, start]]
        visit = set()
        while pq:
            probs, src = heapq.heappop(pq)
            visit.add(src)
            if src == end:
                return probs * -1
            for edge, pr in adj[src]:
                if edge not in visit:
                    heapq.heappush(pq, [probs*pr,edge])
        return 0
