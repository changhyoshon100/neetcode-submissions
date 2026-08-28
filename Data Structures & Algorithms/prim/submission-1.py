import heapq, collections
from typing import List

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visit = set([0])
        minHeap = []
        for v, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, v))

        total = 0
        edges_used = 0

        while edges_used < n - 1:
            if not minHeap:
                return -1  # disconnected

            w, u, v = heapq.heappop(minHeap)
            if v in visit:
                continue

            visit.add(v)
            total += w
            edges_used += 1

            for nei, w2 in adj[v]:
                if nei not in visit:
                    heapq.heappush(minHeap, (w2, v, nei))

        return total
