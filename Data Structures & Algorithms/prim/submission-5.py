class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for n1,n2,w in edges:
            adj[n1].append((n2,w))
            adj[n2].append((n1,w))
        total = 0
        visit = set([0])
        minHeap = []
        for n2,w in adj[0]:
            heapq.heappush(minHeap, (w,0,n2))
        
        while len(visit) < n:
            if not minHeap:
                return -1
            w, n1, n2 = heapq.heappop(minHeap)
            
            if n2 in visit:
                continue
            total += w
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                heapq.heappush(minHeap, (weight, n2, neighbor))
        return total

        