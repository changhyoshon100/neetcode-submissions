class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        arr = list(count.values())
        maxHeap = [i * -1 for i in arr]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time 

            
