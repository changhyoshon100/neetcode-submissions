# import heapq, collections
# from typing import List

# class Solution:
#     def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
#         adj = collections.defaultdict(list)
#         for n1, n2, w in edges:
#             adj[n1].append((n2, w))
#             adj[n2].append((n1, w))

#         visit = set([0])
#         minHeap = []
#         for n2, w in adj[0]:
#             heapq.heappush(minHeap, (w, 0, n2))

#         total = 0
        

#         while len(visit) < n:
#             if not minHeap:
#                 return -1  # disconnected

#             w, n1, n2 = heapq.heappop(minHeap)
#             if n2 in visit:
#                 continue

#             visit.add(n2)
#             total += w
            

#             for nei, w2 in adj[n2]:
#                 if nei not in visit:
#                     heapq.heappush(minHeap, (w2, n2, nei))

#         return total

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for n1, n2, w in edges:
            adj[n1].append((n2, w))
            adj[n2].append((n1, w))
        
        visit = set()
        visit.add((0))
        minHeap = []
        total = 0
        for nei, weight in adj[0]:
            heapq.heappush(minHeap, (weight, 0, nei))
        
        while len(visit) < n:
            if not minHeap:
                return -1
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            visit.add(n2)
            total += weight
            
            for neighbor, weight in adj[n2]:
                heapq.heappush(minHeap, (weight, n2, neighbor))
        return total 

            
        
















