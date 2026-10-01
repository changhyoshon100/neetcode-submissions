class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            pending = []
            used = 0

            for _ in range(n + 1):
                if not heap:
                    break

                freq = heapq.heappop(heap) + 1
                used += 1

                if freq < 0:
                    pending.append(freq)

            for freq in pending:
                heapq.heappush(heap, freq)

            time += n + 1 if heap else used

        return time