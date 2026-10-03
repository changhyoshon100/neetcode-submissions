class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, time in times:
            adj[src].append((dst, time))

        minHeap = [(0, k)]
        shortest = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = time

            for neighbor, travel_time in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(
                        minHeap,
                        (time + travel_time, neighbor)
                    )

        if len(shortest) != n:
            return -1

        return max(shortest.values())