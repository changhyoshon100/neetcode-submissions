class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        time = 0
        count = Counter(tasks)
        count = list(count.values())
        minHeap = [i * -1 for i in count]
        heapq.heapify(minHeap)
        
        while minHeap or q:
            time += 1
            if minHeap:
                cnt = heapq.heappop(minHeap)
                cnt += 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(minHeap, q.popleft()[0])
        return time
